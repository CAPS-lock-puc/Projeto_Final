from models.db import db
from models.iot.devices import Device

class Actuator_pancs(db.Model):
    __tabblename__ = 'actuators_pancs'
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, db.ForeignKey('devices.id'))
    unit = db.Column(db.String(50))
    topic = db.Column(db.String(50))

    def save_actuator_pancs(name, unit, topic, is_active):
        device = Device(name=name, is_active=is_active)
        actuator_abelha = Actuator_pancs(device_id=device.id, unit=unit, topic=topic)

        device.actuators_pancs.append(actuator_abelha)
        db.session.add(device)
        db.session.commit()

    def get_actuators():
        actuators = Actuator_pancs.query.join(Device, Device.id == Actuator_pancs.device_id)\
            .add_columns(Device.id, Device.name, Device.is_active,
                         Actuator_pancs.topic, Actuator_pancs.unit).all()
        return actuators