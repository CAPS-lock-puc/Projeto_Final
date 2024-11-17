from models.db import db
from models.iot.devices import Device

class Sensor(db.Model):
    __tablename__ = 'sensors'
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, db.ForeignKey('devices.id'))
    unit = db.Column(db.String(50))
    topic = db.Column(db.String(50))

    def save_sensor(name, device_id, unit, topic, is_active):
        device = Device(name=name, is_active=is_active)
        sensor = Sensor(device_id=device_id, unit=unit, topic=topic)

        device.sensors.append(sensor)
        db.session.add(device)
        db.session.commit()