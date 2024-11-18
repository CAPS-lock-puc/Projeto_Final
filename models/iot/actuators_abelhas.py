from models.db import db
from models.iot.devices import Device

class Actuator_abelhas(db.Model):
    __tabblename__ = 'actuators_abelhas'
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, db.ForeignKey('devices.id'))
    unit = db.Column(db.String(50))
    topic = db.Column(db.String(50))

    def save_actuator_abelhas(name, unit, topic, is_active):
        device = Device(name=name, is_active=is_active)
        actuator_abelha = Actuator_abelhas(device_id=device.id, unit=unit, topic=topic)

        device.actuators_abelhas.append(actuator_abelha)
        db.session.add(device)
        db.session.commit()