import json
from flask import Flask, render_template, request
from flask_mqtt import Mqtt
from models.db import db, instance
from controllers.sensors_abelhas_controller import sensors_abelhas_
from controllers.actuators_abelhas_controller import actuators_abelhas_
from controllers.historico_abelhas_controller import historico_abelhas
# from controllers.actuators_pancs_controller import actuators_pancs
# from controllers.sensors_pancs_controller import sensors_pancs
# from controllers.historico_pancs_controller import historico_pancs
from models.iot.historico_abelhas import Historico_abelhas

def create_app():
    app = Flask(__name__,
                template_folder="./views/",
                static_folder="./static",
                root_path="./")
    
    app.register_blueprint(sensors_abelhas_, url_prefix='/')
    app.register_blueprint(actuators_abelhas_, url_prefix='/')
    app.register_blueprint(historico_abelhas, url_prefix='/')
    # app.register_blueprint(historico_pancs, url_prefix='/')
    # app.register_blueprint(sensors_pancs, url_prefix='/')
    # app.register_blueprint(actuators_pancs, url_prefix='/')

    app.config['TESTING'] = False
    app.config['SECRET_KEY'] = 'generated-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = instance
    app.config['MQTT_BROKER_URL'] = 'mqtt-dashboard.com'
    app.config['MQTT_BROKER_PORT'] = 1883
    app.config['MQTT_USERNAME'] = ''
    app.config['MQTT_PASSWORD'] = ''
    app.config['MQTT_KEEPALIVE'] = 5000
    app.config['MQTT_TLS_ENABLED'] = False

    mqtt_client = Mqtt()
    mqtt_client.init_app(app)
    db.init_app(app)

    topic_abelhas_sensor = 'abelhas_sensor'
    topic_abelhas_actuator = 'abelhas_actuator'
    
    @app.route('/')
    def index():
        return render_template('home.html')
    
    @app.route('/pancsadm')
    def pancsadm():
        return render_template('pancsadm.html')

    @app.route('/login')
    def login():
        return render_template('login.html')

    @app.route('/admpage')
    def admpage():
        return render_template('admpage.html')
    
    @mqtt_client.on_connect()
    def handle_connect(client, userdata, flags, rc):
        if rc == 0:
            mqtt_client.subscribe(topic_abelhas_sensor)
            mqtt_client.subscribe(topic_abelhas_actuator)
            print("Broker Connected Successfully")
        else:
            print('Bad Connection Returned code=', rc)

    @mqtt_client.on_message()
    def handle_mqtt_message(client, userdata, message):
        print(f"Mensagem recebida no tópico {message.topic}: {message.payload.decode()}")

        try:
            js = json.loads(message.payload.decode())
            print(f"Mensagem decodificada: {js}")

            if message.topic == topic_abelhas_sensor:
                with app.app_context():
                    Historico_abelhas.save_historico_abelhas(js["sensor"], js["valor"])
                    print(f"Salvou leitura no banco: {js}")
        except Exception as e:
            print(f"Erro: {e}")

    
    return app