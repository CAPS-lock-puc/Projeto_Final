from models.db import db
from models.iot.devices import Device
from models.iot.sensors_pancs import Sensor_pancs

class Actuator_pancs(db.Model):
    __tabblename__ = 'actuators_pancs'
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, db.ForeignKey('devices.id'))
    unit = db.Column(db.String(50))
    topic = db.Column(db.String(50))

    def save_actuator_pancs(name, unit, topic, is_active):
        device = Device(name=name, is_active=is_active)
        actuator_pancs = Actuator_pancs(device_id=device.id, unit=unit, topic=topic)

        device.actuators_pancs.append(actuator_pancs)
        db.session.add(device)
        db.session.commit()

    def get_actuators():
        actuators = Actuator_pancs.query.join(Device, Device.id == Actuator_pancs.device_id)\
            .add_columns(Device.id, Device.name, Device.is_active,
                         Actuator_pancs.topic, Actuator_pancs.unit).all()
        return actuators
    
    def get_single_actuator(id):
        actuator = Actuator_pancs.query.filter(Actuator_pancs.device_id==id).first()
        if actuator is not None:
            actuator = Actuator_pancs.query.filter(Actuator_pancs.device_id==id)\
                .join(Device).add_columns(Device.id, Device.name, Device.is_active,
                                          Actuator_pancs.topic, Actuator_pancs.unit).first()
            return [actuator]
        
    def deactivate_actuators():
        actuators = Actuator_pancs.query.all()
        for actuator in actuators:
            actuator.device.is_active = False
            db.session.add(actuator.device)
        db.session.commit()

    def activate_actuators():
        actuators = Actuator_pancs.query.all()
        for actuator in actuators:
            actuator.device.is_active = True
            db.session.add(actuator.device)
        db.session.commit()

    def update_actuator_pancs(id, name, unit, topic, is_active):
        device = Device.query.filter(Device.id==id).first()
        actuator_pancs = Actuator_pancs.query.filter(Actuator_pancs.device_id==id).first()
        if device is not None:
            device.name = name
            actuator_pancs.unit = unit
            actuator_pancs.topic = topic
            device.is_active = is_active
            db.session.commit()
            return Actuator_pancs.get_actuators()
        
    def delete_actuator_pancs(id):
        device = Device.query.filter(Device.id==id).first()
        actuator = Actuator_pancs.query.filter(Actuator_pancs.device_id==id).first()

        db.session.delete(actuator)
        db.session.delete(device)
        db.session.commit()

        return Actuator_pancs.get_actuators()