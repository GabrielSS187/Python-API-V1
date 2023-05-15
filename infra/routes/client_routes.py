# -*- coding: utf-8 -*-

import os
from app import db
from app import load_dotenv
from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
import hashlib
from datetime import timedelta
import uuid

from errors.client_errors import ClientValidator
from models.client_model import Client
from models.account_model import Account
from models.contract_product_model import ContractProduct
from models.product_model import Product
from errors.custom_error import CustomError

load_dotenv()

client_routes = Blueprint('client', __name__)


@client_routes.route('/clients', methods=['GET'])
@jwt_required()
def get_client_by_token():
    current_client = get_jwt_identity()
    client = Client.query.filter_by(id=current_client).first()
    account = Account.query.filter_by(id=client.account_id).first()

    query_contracts = (
        db.session.query(ContractProduct)
        .join(Account, Account.id == ContractProduct.account_id)
        .filter(Account.id == client.account_id)
    )

    product_ids = []
    for contract_product in query_contracts.all():
        product_ids.append(contract_product.product_id)

    query_products = db.session.query(
        Product).filter(Product.id.in_(product_ids))

    products = []
    for product in query_products.all():
        products.append({
            'id': product.id,
            'name': product.name,
            'value': product.value,
            'type': product.type,
        })

    contracts_total_value = sum(product['value'] for product in products)
    user_info = {
        'client_id': client.id,
        'client_name': client.name,
        'client_email': client.email,
        'client_password': client.password,
        'account_info': {
                'account_id': account.id,
                 'account_name': account.name_account,
            },
        'contracted_products': {
            'total_value': contracts_total_value,
            'products': products,
        }
    }

    return jsonify(user_info), 200


@client_routes.route('/clients/all', methods=['GET'])
def get_all_clients():
    clients = db.session.query(Client, Account).join(Account).all()

    result = []
    for client, account in clients:
        result.append({
            'id': client.id,
            'name': client.name,
            'email': client.email,
            'hash_password': client.password,
            'account': {
                'id': account.id,
                'account_name': account.name_account,
            }
        })

    return jsonify(result), 200


@client_routes.route('/clients/contract_product/<int:product_id>', methods=['GET'])
@jwt_required()
def client_contract_product(product_id):
    current_client = get_jwt_identity()

    product = Product.query.filter_by(id=product_id).first()
    if not product:
        raise CustomError('Product not found.', 404)

    client = Client.query.filter_by(id=current_client).first()

    newContract = ContractProduct(
        id=str(uuid.uuid4()),
        account_id=client.account_id,
        product_id=product_id
    )
    db.session.add(newContract)
    db.session.commit()

    return jsonify({'message': 'Contracted product success.'}), 200


@client_routes.route('/clients/create', methods=['POST'])
def create_client():
    data = request.get_json()

    request_validadetor = {
        'name': data['name'],
        'email': data['email'],
        'password': data['password'],
    }

    ClientValidator(**request_validadetor)

    user = Client.query.filter_by(email=request_validadetor['email']).first()
    if user:
        raise CustomError('A client with that email already exists.', 409)

    account_id = str(uuid.uuid4())
    first_sequence = account_id.split("-")[0]
    name_account = first_sequence+'-'+request_validadetor['email']

    hash_password = hashlib.sha256(os.getenv('SALT').encode(
    ) + request_validadetor['password'].encode()).hexdigest()
    print(hash_password)
    request_validadetor['password'] = hash_password

    new_account = Account(
        id=account_id,
        name_account=name_account
    )
#
    new_client = Client(
        **request_validadetor,
        account_id=account_id,
    )
    db.session.add(new_account)
    db.session.add(new_client)
    db.session.commit()

    return jsonify({'message': 'Client successfully created.'}), 201


@client_routes.route('/clients/login', methods=['POST'])
def client_login():
    data = request.get_json()

    if not data.get('email') and not data.get('password'):
        raise CustomError('Email and password are required.', 406)

    user = Client.query.filter_by(email=data['email']).first()

    if not user:
        raise CustomError('User not found.', 404)

    hash_password = hashlib.sha256(
        os.getenv('SALT').encode() + data.get('password').encode()).hexdigest()

    if user.password != hash_password:
        raise CustomError('Incorrect password', 406)

    generate_token = create_access_token(
        identity=user.id, expires_delta=timedelta(minutes=60))

    return jsonify({'client_name': user.name, 'access_token': generate_token}), 200
