from app import db

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    account_id = db.Column(db.String(255), db.ForeignKey('account.id', ondelete='CASCADE'), nullable=False)
