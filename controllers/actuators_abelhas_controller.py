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

    return redirect(url_for('actuators_abelhas.register_actuator_abelhas'))