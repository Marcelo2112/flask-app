from functools import wraps
from flask import request, jsonify, Blueprint
from project import db
from project.models import Proveedor
from project.schemas import proveedor_schema
from project.endpoints.users import autenticar

blueprint = Blueprint('proveedor', __name__)


@blueprint.route ('/registerinsumo', methods=['GET'])
@autenticar
def list(usuario):
    proveedor = Proveedor.query.all()
    print(proveedor)

    return jsonify(proveedor_schema.dump(proveedor, many=True)), 200 


@blueprint.route('/registerinsumo', methods=['POST'])
@autenticar
def regis(usuario):

    proveedor = proveedor_schema.load(request.json)

    db.session.add(proveedor)
    db.session.commit()

    return proveedor_schema.dump(proveedor),201


