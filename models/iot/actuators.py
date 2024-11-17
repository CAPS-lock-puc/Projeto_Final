from models.db import db
from models.iot.devices import Device

class Actuator(db.Model):
    __tabblename__ = 'actuators'
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, db.ForeignKey('devices.id'))
    unit = db.Column(db.String(50))
    topic = db.Column(db.String(50))