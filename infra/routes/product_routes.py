# -*- coding: utf-8 -*-

from app import db
from flask import Blueprint, jsonify, request

from errors.product_errors import PoductValidatorOptional, PoductValidator
from models.product_model import Product
from errors.custom_error import CustomError

product_routes = Blueprint('product', __name__)


@product_routes.route('/products', methods=['GET'])
def get_all_products():
    products = Product.query.all()
    result = [{'id': product.id, 'name': product.name,
               'value': product.value, 'type': product.type} for product in products]
    return jsonify(result), 200


@product_routes.route('/products/register', methods=['POST'])
def register_product():
    data = request.get_json()

    request_data = {
        'name': data['name'],
        'value': data['value'],
        'type': data['type'],
    }

    product_validator = PoductValidator(**request_data).dict()

    product = Product.query.filter_by(name=request_data['name']).first()
    if product:
        raise CustomError('A product with that name already exists.', 409)

    new_product = Product(**product_validator)
    db.session.add(new_product)
    db.session.commit()

    return jsonify({'message': 'Product created successfully.'}), 201


@product_routes.route('/products/edit/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()

    product_data = PoductValidatorOptional(**data).dict()
    product_data = {k: v for k, v in product_data.items() if v}

    product = Product.query.get(product_id)

    if not product:
        raise CustomError('Product not found.', 404)

    if 'name' in product_data:
        product_exist = Product.query.filter_by(
            name=product_data['name']).first()
        if product_exist and product_exist.id != product.id:
            raise CustomError('A product with that name already exists.', 409)

    if product_data.get('name'):
        product.name = product_data['name']
    if product_data.get('value'):
        product.value = product_data['value']
    if product_data.get('type'):
        product.type = product_data['type']

    db.session.commit()

    return jsonify({'message': 'Product updated successfully'})


@product_routes.route('/products/delete/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.filter_by(id=product_id).first()

    if not product:
        raise CustomError('Product not found.', 404)

    db.session.delete(product)
    db.session.commit()

    return jsonify({'message': 'Product deleted successfully.'})
