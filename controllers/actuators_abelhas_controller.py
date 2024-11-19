from flask import Blueprint, request, render_template, redirect, url_for
from models.iot.actuators_abelhas import Actuator_abelhas

actuators_abelhas_ = Blueprint('actuators_abelhas', __name__, template_folder='views')

@actuators_abelhas_.route('/add_actuator_abelhas', methods=['POST'])
def add_actuator_abelhas():
    name = request.form['name']
    topic = request.form['topic']
    unit = request.form['unit']
    is_active = True if request.form.get("is_active") == "on" else False

    Actuator_abelhas.save_actuator_abelhas(name, topic, unit, is_active)

    return redirect(url_for('sensor_abelhas.abelhasadm'))

@actuators_abelhas_.route('/edit_actuator_abelhas')
def edit_actuator_abelhas():
    id = request.args.get('id', None)
    actuators = Actuator_abelhas.get_single_actuator(id)
    return render_template('update_actuator_abelhas.html', actuators=actuators)

@actuators_abelhas_.route('/update_actuator_abelhas', methods=['POST'])
def update_actuator_abelhas():
    id = request.form['id']
    name = request.form['name']
    topic = request.form['topic']
    unit = request.form['unit']
    is_active = True if request.form.get("is_active") == "on" else False

    Actuator_abelhas.update_actuator_abelhas(id, name, topic, unit, is_active)

    return redirect(url_for('sensor_abelhas.abelhasadm'))