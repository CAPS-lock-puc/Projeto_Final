from models.db import db
from models.iot.devices import Device
from models.iot.sensors_abelhas import Sensor_abelhas

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

    def get_actuators():
        actuators = Actuator_abelhas.query.join(Device, Device.id == Actuator_abelhas.device_id)\
            .add_columns(Device.id, Device.name, Device.is_active,
                         Actuator_abelhas.topic, Actuator_abelhas.unit).all()
        return actuators
    
    def get_single_actuator(id):
        actuator = Actuator_abelhas.query.filter(Actuator_abelhas.device_id==id).first()
        if actuator is not None:
            actuator = Actuator_abelhas.query.filter(Actuator_abelhas.device_id==id)\
                .join(Device).add_columns(Device.id, Device.name, Device.is_active,
                                          Actuator_abelhas.topic, Actuator_abelhas.unit).first()
            return [actuator]
    
    def deactivate_actuators():
        actuators = Actuator_abelhas.query.all()
        for actuator in actuators:
            actuator.device.is_active = False
            db.session.add(actuator.device)
        db.session.commit()

    def activate_actuators():
        actuators = Actuator_abelhas.query.all()
        for actuator in actuators:
            actuator.device.is_active = True
            db.session.add(actuator.device)
        db.session.commit()

    def update_actuator_abelhas(id, name, unit, topic, is_active):
        device = Device.query.filter(Device.id==id).first()
        actuator_abelhas = Actuator_abelhas.query.filter(Actuator_abelhas.device_id==id).first()
        if device is not None:
            device.name = name
            actuator_abelhas.unit = unit
            actuator_abelhas.topic = topic
            device.is_active = is_active
            db.session.commit()
            return Actuator_abelhas.get_actuators()
        
    def delete_actuator_abelhas(id):
        device = Device.query.filter(Device.id==id).first()
        actuator = Actuator_abelhas.query.filter(Actuator_abelhas.device_id==id).first()

        db.session.delete(actuator)
        db.session.delete(device)
        db.session.commit()

        return Actuator_abelhas.get_actuators()