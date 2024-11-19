from flask import Blueprint, request, render_template, redirect, url_for

peixes = Blueprint('peixes', __name__, template_folder='views')



@peixes.route('/peixesadm')
def peixesadm():
    return render_template('peixesadm.html')

@peixes.route('/peixes')
def mostrar_peixes():
    return render_template('peixes.html')
