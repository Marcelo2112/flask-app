from flask import Blueprint


blueprint= Blueprint('status', __name__)



@blueprint.route('/')
def index():
    return '<h1>Hola uwu</h1>'