from flask import Blueprint, request, render_template, redirect, url_for
from models.iot.actuators_pancs import Actuator_pancs

actuators_pancs_ = Blueprint('actuators_pancs', __name__, template_folder='views')

@actuators_pancs_.route('/add_actuator_pancs', methods=['POST'])
def add_actuator_pancs():
    name = request.form['name']
    topic = request.form['topic']
    unit = request.form['unit']
    is_active = True if request.form.get("is_active") == "on" else False

    Actuator_pancs.save_actuator_pancs(name, topic, unit, is_active)

    return redirect(url_for('sensor_pancs.pancsadm'))

@actuators_pancs_.route('/edit_actuator_pancs')
def edit_actuator_pancs():
    id = request.args.get('id', None)
    actuators = Actuator_pancs.get_single_actuator(id)
    return render_template('update_actuator_pancs.html', actuators=actuators)

@actuators_pancs_.route('/update_actuator_pancs', methods=['POST'])
def update_actuator_pancs():
    id = request.form['id']
    name = request.form['name']
    topic = request.form['topic']
    unit = request.form['unit']
    is_active = True if request.form.get("is_active") == "on" else False

    Actuator_pancs.update_actuator_pancs(id, name, topic, unit, is_active)

    return redirect(url_for('sensor_pancs.pancsadm'))

@actuators_pancs_.route('/del_actuator_pancs', methods=['GET'])
def del_actuator_pancs():
    id = request.args.get('id', None)
    Actuator_pancs.delete_actuator_pancs(id)
    return redirect(url_for('sensor_pancs.pancsadm'))