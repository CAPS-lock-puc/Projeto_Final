from flask import Flask, render_template, request
from models.db import db, instance
from controllers.sensors_abelhas_controller import sensors_abelhas_
from controllers.actuators_abelhas_controller import actuators_abelhas_

def create_app():
    app = Flask(__name__,
                template_folder="./views/",
                static_folder="./static",
                root_path="./")
    
    app.register_blueprint(sensors_abelhas_, url_prefix='/')
    app.register_blueprint(actuators_abelhas_, url_prefix='/')

    app.config['TESTING'] = False
    app.config['SECRET_KEY'] = 'generated-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = instance

    db.init_app(app)
    
    @app.route('/')
    def index():
        return render_template('home.html')
    
    return app