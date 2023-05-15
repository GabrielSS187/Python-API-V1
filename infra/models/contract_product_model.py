import uuid
from app import db

class ContractProduct(db.Model):
    id = db.Column(db.String(255), primary_key=True, nullable=False)
    account_id = db.Column(db.String(255), db.ForeignKey('account.id', ondelete='CASCADE'), nullable=False)
    product_id = db.Column(db.Integer(), db.ForeignKey('product.id', ondelete='CASCADE'), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
