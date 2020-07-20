import requests
from functools import wraps
from flask import request, jsonify, Blueprint
from project import db
from project.models import Proveedor
from project.schemas import proveedor_schema


blueprint = Blueprint('proveedor', __name__)


def check_token():
    authorization = request.headers.get('Authorization')

    response = requests.get(
        'http://localhost:5000/token',
        headers={'Authorization': authorization}
    )

    if response.ok:
        return response.json()
    return False


def autenticar(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        check_response = check_token()
        if check_response is False:
            return 'Unauthorized', 401
        return f(check_response, *args, **kwargs)
    return wrapper

@blueprint.route('/registroinsumoo', methods=['POST'])
@autenticar 
def registro(usuario):
    print(usuario)
    datos = request.json
    datos [' usuario_id'] = usuario ['id']
    proveedor = proveedor_schema.load(datos)

    db.session.add(proveedor)
    db.session.commit()

    return proveedor_schema.dump(proveedor), 201
 



