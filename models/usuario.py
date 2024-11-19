class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    senha = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # ADM ou usuario