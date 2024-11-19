from flask import Blueprint, request, render_template, redirect, url_for

vacas = Blueprint('vacas', __name__, template_folder='views')



@vacas.route('/vacasadm')
def vacasadm():
    return render_template('vacasadm.html')

@vacas.route('/vacas')
def mostrar_vacas():
    return render_template('vacas.html')
