from flask import Blueprint, request, render_template, redirect, url_for
from models.iot.historico_abelhas import Historico_abelhas
from models.iot.sensors_abelhas import Sensor_abelhas

historico_abelhas = Blueprint('historico_abelhas', __name__, template_folder='views')

@historico_abelhas.route('/get_historico_abelhas', methods=['POST'])
def get_historico_abelhas():
    if request.method == 'POST':
        id = request.form['id']
        start = request.form['start']
        end = request.form['end']
        historico_abelhas = Historico_abelhas.get_historico_abelhas(id, start ,end)

        sensors= Sensor_abelhas.get_sensors()
        return render_template('abelhasadm.html', historico_abelhas=historico_abelhas, sensors=sensors)