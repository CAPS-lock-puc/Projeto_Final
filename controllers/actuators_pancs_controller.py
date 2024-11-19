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