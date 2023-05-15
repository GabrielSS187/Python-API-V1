from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    value = db.Column(db.Float, nullable=False)
    type = db.Column(db.Enum('Recorrente', 'Avulso', name='product_type'), nullable=False)    
