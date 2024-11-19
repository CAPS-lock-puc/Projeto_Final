from flask import Blueprint, request, render_template, redirect, url_for
from models.iot.historico_pancs import Historico_pancs
from models.iot.sensors_pancs import Sensor_pancs
from models.iot.actuators_pancs import Actuator_pancs

historico_pancs = Blueprint('historico_pancs', __name__, template_folder='views')

@historico_pancs.route('/get_historico_pancs', methods=['POST'])
def get_historico_pancs():
    if request.method == 'POST':
        id = request.form['id']
        start = request.form['start']
        end = request.form['end']
        historico_pancs = Historico_pancs.get_historico_pancs(id, start ,end)

        sensors= Sensor_pancs.get_sensors()
        actuators = Actuator_pancs.get_actuators()
        return render_template('pancsadm.html', historico_pancs=historico_pancs,
                                                    sensors=sensors, actuators=actuators)