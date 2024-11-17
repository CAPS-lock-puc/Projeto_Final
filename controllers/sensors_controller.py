from flask import Blueprint, request, render_template, redirect, url_for
from models.iot.sensors_abelhas import Sensor_abelhas

sensors_abelhas = Blueprint('sensor_abelhas', __name__, template_folder='views')