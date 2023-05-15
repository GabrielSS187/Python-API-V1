from app import db

class Account(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    name_account = db.Column(db.String(80), nullable=False)