from models.db import db
from models.iot.sensors_abelhas import Sensor_abelhas
from models.iot.devices import Device
from datetime import datetime

class Historico_abelhas(db.Model):
    __tablename__ = 'historico_abelhas'
    id = db.Column('id',db.Integer, primary_key=True)
    data = db.Column(db.DateTime(), nullable=False)
    sensor_abelhas_id = db.Column(db.Integer, db.ForeignKey(Sensor_abelhas.id), nullable=False)
    value = db.Column(db.Float, nullable=False)

    def save_historico_abelhas(id, value):
        sensor_abelhas = Sensor_abelhas.query.filter(Sensor_abelhas.id == id).first()
        device = Device.query.filter(Device.id == sensor_abelhas.device_id).first()
        if (sensor_abelhas is not None)and (device.is_active==True):
            historico_abelhas = Historico_abelhas(data=datetime.now(),
                                                  sensor_abelhas_id=sensor_abelhas.id,
                                                  value=float(value))
            db.session.add(historico_abelhas)
            db.session.commit()

    def get_historico_abelhas(device_id, start, end):
        sensor_abelhas = Sensor_abelhas.query.filter(Sensor_abelhas.device_id == device_id).first()
        historico_abelhas = Historico_abelhas.query.filter(Historico_abelhas.sensor_abelhas_id == sensor_abelhas.id,
                                                           Historico_abelhas.data >= start,
                                                           Historico_abelhas.data <= end).all()
        return historico_abelhas        
    
    def get_last_value_abelhas(sensor_id):
        last_entry = Historico_abelhas.query.filter(
            Historico_abelhas.sensor_abelhas_id == sensor_id
        ).order_by(Historico_abelhas.data.desc()).first()
        return last_entry.value if last_entry else None