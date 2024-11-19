from flask import Blueprint, request, render_template, redirect, url_for
from models.iot.historico_abelhas import Historico_abelhas
from models.iot.sensors_abelhas import Sensor_abelhas
from models.iot.actuators_abelhas import Actuator_abelhas

historico_abelhas = Blueprint('historico_abelhas', __name__, template_folder='views')

@historico_abelhas.route('/get_historico_abelhas', methods=['POST'])
def get_historico_abelhas():
    if request.method == 'POST':
        id = request.form['id']
        start = request.form['start']
        end = request.form['end']
        historico_abelhas = Historico_abelhas.get_historico_abelhas(id, start, end)

        sensors = Sensor_abelhas.get_sensors()
        actuators = Actuator_abelhas.get_actuators()
        last_values = {
            sensor.id: Historico_abelhas.get_last_value(sensor.id)
            for sensor in sensors
        }

        if any(value is not None and value < 50 for value in last_values.values()):
                Actuator_abelhas.deactivate_actuators()
        elif any (value is not None and value >= 50 for value in last_values.values()):
                Actuator_abelhas.activate_actuators()

        return render_template('abelhasadm.html',
                               historico_abelhas=historico_abelhas,
                               sensors=sensors,
                               actuators=actuators,
                               last_values=last_values)
