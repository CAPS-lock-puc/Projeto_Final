from models import db

class Device(db.Model):
    __tablename__ = 'devices'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    is_active = db.Column(db.Boolean, nullable=False, default=False)

    sensors_abelhas = db.relationship('Sensor_abelhas', backref='device', lazy=True)
    actuators_abelhas = db.relationship('Actuator_abelhas', backref='device', lazy=True)
    sensors_pancs = db.relationship('Sensor_pancs', backref='device', lazy=True)
    actuators_pancs = db.relationship('Actuator_pancs', backref='device', lazy=True)