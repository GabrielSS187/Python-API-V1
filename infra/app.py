# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring

import os
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

from errors.custom_error import CustomError

load_dotenv()

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_KEY')

db = SQLAlchemy(app)
jwt = JWTManager(app)

from routes.product_routes import product_routes
from routes.client_routes import client_routes

app.register_blueprint(product_routes)
app.register_blueprint(client_routes)

@app.errorhandler(Exception)
def handle_exception(error):
    if isinstance(error, CustomError):
        response = jsonify({'error': str(error)})
        response.status_code = error.status_code
        return response
    response = jsonify({'error': str(error)})
    response.status_code = 500
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 8000)))
