class Sensor(db.Model):
    __tablename__ = 'sensores'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)  # abelhas, vacas
    leitura_atual = db.Column(db.String(200), nullable=True)
    device_id = db.Column(db.Integer, db.ForeignKey('devices.id'), nullable=False)