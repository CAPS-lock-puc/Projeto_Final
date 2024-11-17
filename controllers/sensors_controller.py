from flask import Blueprint, request, render_template, redirect, url_for
from models.iot.sensors import Sensor

sensors = Blueprint('sensor_', __name__, template_folder='views')