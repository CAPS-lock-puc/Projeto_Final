from models.db import db
from models.iot.devices import Device

class Sensor_pancs(db.Model):
    __tablename__ = 'sensors_pancs'
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, db.ForeignKey('devices.id'))
    unit = db.Column(db.String(50))
    topic = db.Column(db.String(50))

    def save_sensor_pancs(name, unit, topic, is_active):
        device = Device(name=name, is_active=is_active)
        sensor_pancs = Sensor_pancs(device_id=device.id, unit=unit, topic=topic)

        device.sensors_pancs.append(sensor_pancs)
        db.session.add(device)
        db.session.commit()

    def get_sensors():
        sensors = Sensor_pancs.query.join(Device, Device.id == Sensor_pancs.device_id)\
            .add_columns(Device.id, Device.name, Device.is_active,
                         Sensor_pancs.topic, Sensor_pancs.unit).all()
        return sensors
    
    def get_single_sensor(id):
        sensor = Sensor_pancs.query.filter(Sensor_pancs.device_id==id).first()
        if sensor is not None:
            sensor = Sensor_pancs.query.filter(Sensor_pancs.device_id==id)\
                .join(Device).add_columns(Device.id, Device.name, Device.is_active,
                                          Sensor_pancs.topic, Sensor_pancs.unit).first()
            return [sensor] 
    
    def update_sensor_pancs(id, name, unit, topic, is_active):
        device = Device.query.filter(Device.id==id).first()
        sensor_pancs = Sensor_pancs.query.filter(Sensor_pancs.device_id==id).first()
        if device is not None:
            device.name = name
            sensor_pancs.unit = unit
            sensor_pancs.topic = topic
            device.is_active = is_active
            db.session.commit()
            return Sensor_pancs.get_sensors()
        
    def delete_sensor_pancs(id):
        device = Device.query.filter(Device.id==id).first()
        sensor = Sensor_pancs.query.filter(Sensor_pancs.device_id==id).first()

        db.session.delete(sensor)
        db.session.delete(device)
        db.session.commit()

        return Sensor_pancs.get_sensors()