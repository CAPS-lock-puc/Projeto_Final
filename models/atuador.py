class Atuador(db.Model):
    __tablename__ = 'atuadores'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)  #  pancs, peixes
    estado_atual = db.Column(db.String(100), nullable=False)  # estado ( liberado, fechado)
    device_id = db.Column(db.Integer, db.ForeignKey('devices.id'), nullable=False)
