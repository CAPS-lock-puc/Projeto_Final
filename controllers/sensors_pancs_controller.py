from flask import Blueprint, request, render_template, redirect, url_for
from models.iot.sensors_pancs import Sensor_pancs
from models.iot.actuators_pancs import Actuator_pancs

sensors_pancs_ = Blueprint('sensor_pancs', __name__, template_folder='views')

@sensors_pancs_.route('/pancsadm')
def pancsadm():
    sensors = Sensor_pancs.get_sensors()
    actuators = Actuator_pancs.get_actuators()
    return render_template('pancsadm.html', sensors=sensors, actuators=actuators)

@sensors_pancs_.route('/add_sensor_pancs', methods=['POST'])
def add_sensor_pancs():
    name = request.form['name']
    topic = request.form['topic']
    unit = request.form['unit']
    is_active = True if request.form.get("is_active") == "on" else False

    Sensor_pancs.save_sensor_pancs(name, topic, unit, is_active)

    return redirect(url_for('sensor_pancs.pancsadm'))

@sensors_pancs_.route('/edit_sensor_pancs')
def edit_sensor_pancs():
    id = request.args.get('id', None)
    sensor = Sensor_pancs.get_single_sensor(id)
    return render_template('update_sensor_pancs.html', sensor=sensor)

@sensors_pancs_.route('/update_sensor_pancs', methods=['POST'])
def update_sensor_pancs():
    id = request.form['id']
    name = request.form['name']
    topic = request.form['topic']
    unit = request.form['unit']
    is_active = True if request.form.get("is_active") == "on" else False

    Sensor_pancs.update_sensor_pancs(id, name, topic, unit, is_active)

    return redirect(url_for('sensor_pancs.pancsadm'))

@sensors_pancs_.route('/del_sensor_pancs', methods=['GET'])
def del_sensor_pancs():
    id = request.args.get('id', None)
    Sensor_pancs.delete_sensor_pancs(id)
    return redirect(url_for('sensor_pancs.pancsadm'))