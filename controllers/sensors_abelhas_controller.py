from flask import Blueprint, request, render_template, redirect, url_for
from models.iot.sensors_abelhas import Sensor_abelhas

sensors_abelhas_ = Blueprint('sensor_abelhas', __name__, template_folder='views')

@sensors_abelhas_.route('/register_sensor_abelhas')
def register_sensor_abelhas():
    return render_template('abelhasadm.html')

@sensors_abelhas_.route('/add_sensor_abelhas', methods=['POST'])
def add_sensor_abelhas():
    name = request.form.get['name']
    unit = request.form.get['unit']
    topic = request.form.get['topic']
    is_active = True if request.form.get['is_active'] == 'on' else False

    Sensor_abelhas.save_sensor_abelhas(name, unit, topic, is_active)

    return redirect(url_for('sensor_abelhas.sensor_abelhas'))