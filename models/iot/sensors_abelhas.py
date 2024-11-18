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