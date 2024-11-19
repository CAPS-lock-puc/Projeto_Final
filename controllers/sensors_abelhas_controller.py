from flask import Blueprint, request, render_template, redirect, url_for
from models.iot.sensors_abelhas import Sensor_abelhas
from models.iot.actuators_abelhas import Actuator_abelhas

sensors_abelhas_ = Blueprint('sensor_abelhas', __name__, template_folder='views')

@sensors_abelhas_.route('/abelhasadm')
def abelhasadm():
    sensors = Sensor_abelhas.get_sensors()
    actuators = Actuator_abelhas.get_actuators()
    return render_template('abelhasadm.html', sensors=sensors, actuators=actuators)

@sensors_abelhas_.route('/add_sensor_abelhas', methods=['POST'])
def add_sensor_abelhas():
    name = request.form['name']
    topic = request.form['topic']
    unit = request.form['unit']
    is_active = True if request.form.get("is_active") == "on" else False

    Sensor_abelhas.save_sensor_abelhas(name, topic, unit, is_active)

    return redirect(url_for('sensor_abelhas.abelhasadm'))

@sensors_abelhas_.route('/edit_sensor_abelhas')
def edit_sensor_abelhas():
    id = request.args.get('id', None)
    sensor = Sensor_abelhas.get_single_sensor(id)
    return render_template('update_sensor_abelhas.html', sensor=sensor)

@sensors_abelhas_.route('/update_sensor_abelhas', methods=['POST'])
def update_sensor_abelhas():
    id = request.form['id']
    name = request.form['name']
    topic = request.form['topic']
    unit = request.form['unit']
    is_active = True if request.form.get("is_active") == "on" else False

    Sensor_abelhas.update_sensor_abelhas(id, name, topic, unit, is_active)

    return redirect(url_for('sensor_abelhas.abelhasadm'))

@sensors_abelhas_.route('/del_sensor_abelhas', methods=['GET'])
def del_sensor_abelhas():
    id = request.args.get('id', None)
    sensor = Sensor_abelhas.delete_sensor_abelhas(id)
    return redirect(url_for('sensor_abelhas.abelhasadm'))