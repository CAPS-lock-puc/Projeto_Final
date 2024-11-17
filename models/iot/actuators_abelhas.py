from models.db import db
from models.iot.devices import Device

class Actuator_abelhas(db.Model):
    __tabblename__ = 'actuators_abelhas'
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, db.ForeignKey('devices.id'))
    unit = db.Column(db.String(50))
    topic = db.Column(db.String(50))