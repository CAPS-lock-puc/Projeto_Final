from models.db import db
from models.iot.devices import Device

class Sensor_abelhas(db.Model):
    __tablename__ = 'sensors_abelhas'
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, db.ForeignKey('devices.id'))
    unit = db.Column(db.String(50))
    topic = db.Column(db.String(50))

    def save_sensor_abelhas(name, unit, topic, is_active):
        device = Device(name=name, is_active=is_active)
        sensor_abelha = Sensor_abelhas(device_id=device.id, unit=unit, topic=topic)

        device.sensors_abelhas.append(sensor_abelha)
        db.session.add(device)
        db.session.commit()

    def get_sensors():
        sensors = Sensor_abelhas.query.join(Device, Device.id == Sensor_abelhas.device_id)\
            .add_columns(Device.id, Device.name, Device.is_active,
                         Sensor_abelhas.topic, Sensor_abelhas.unit).all()
        return sensors
    
    def get_single_sensor(id):
        sensor = Sensor_abelhas.query.filter(Sensor_abelhas.device_id==id).first()
        if sensor is not None:
            sensor = Sensor_abelhas.query.filter(Sensor_abelhas.device_id==id)\
                .join(Device).add_columns(Device.id, Device.name, Device.is_active,
                                          Sensor_abelhas.topic, Sensor_abelhas.unit).first()
            return [sensor] 
        
    def update_sensor_abelhas(id, name, unit, topic, is_active):
        device = Device.query.filter(Device.id==id).first()
        sensor_abelhas = Sensor_abelhas.query.filter(Sensor_abelhas.device_id==id).first()
        if device is not None:
            device.name = name
            sensor_abelhas.unit = unit
            sensor_abelhas.topic = topic
            device.is_active = is_active
            db.session.commit()
            return Sensor_abelhas.get_sensors()