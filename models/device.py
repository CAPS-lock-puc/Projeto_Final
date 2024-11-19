class Device(db.Model):
    __tablename__ = 'devices'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)  # sensor ou atuador
    historicos = db.relationship('Historico', backref='device', lazy=True)