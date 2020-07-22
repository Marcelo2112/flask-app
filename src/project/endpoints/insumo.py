from functools import wraps
from flask import request, jsonify, Blueprint
from project import db
from project.models import Insumo
from project.schemas import insumo_schema
from project.endpoints.users import autenticar

blueprint = Blueprint('insumo', __name__)


@blueprint.route ('/registerinsumo2', methods=['GET'])
@autenticar
def list(usuario):
    insumo = Insumo.query.all()
    print(insumo)

    return jsonify(insumo_schema.dump(insumo, many=True)), 200 


@blueprint.route('/registerinsumo2', methods=['POST'])
@autenticar
def regis(usuario):
    



    insumo = insumo_schema.load(request.json)

    db.session.add(insumo)
    db.session.commit()

    return insumo_schema.dump(insumo),201