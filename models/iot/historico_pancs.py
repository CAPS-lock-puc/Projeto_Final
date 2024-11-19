from models.db import db
from models.iot.sensors_pancs import Sensor_pancs
from models.iot.devices import Device
from datetime import datetime

class Historico_pancs(db.Model):
    __tablename__ = 'historico_pancs'
    id = db.Column('id',db.Integer, primary_key=True)
    data = db.Column(db.DateTime(), nullable=False)
    sensor_pancs_id = db.Column(db.Integer, db.ForeignKey(Sensor_pancs.id), nullable=False)
    value = db.Column(db.Float, nullable=False)

    def save_historico_pancs(id, value):
        sensor_pancs = Sensor_pancs.query.filter(Sensor_pancs.id == id).first()
        device = Device.query.filter(Device.id == sensor_pancs.device_id).first()
        if (sensor_pancs is not None)and (device.is_active==True):
            historico_pancs = Historico_pancs(data=datetime.now(),
                                                  sensor_pancs_id=sensor_pancs.id,
                                                  value=float(value))
            db.session.add(historico_pancs)
            db.session.commit()

    def get_historico_pancs(device_id, start, end):
        sensor_pancs = Sensor_pancs.query.filter(Sensor_pancs.device_id == device_id).first()
        historico_pancs = Historico_pancs.query.filter(Historico_pancs.sensor_pancs_id == sensor_pancs.id,
                                                           Historico_pancs.data >= start,
                                                           Historico_pancs.data <= end).all()
        return historico_pancs        