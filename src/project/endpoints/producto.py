from functools import wraps
from flask import request, jsonify, Blueprint
from project import db
from project.models import Producto
from project.schemas import producto_schema
from project.endpoints.users import autenticar

blueprint = Blueprint('producto', __name__)


@blueprint.route ('/registerinsumo3', methods=['GET'])
@autenticar
def list(usuario):
    producto = Producto.query.all()
    print(producto)

    return jsonify(producto_schema.dump(producto, many=True)), 200 


@blueprint.route('/registerinsumo3', methods=['POST'])
@autenticar
def regis(usuario):

    producto = producto_schema.load(request.json)

    db.session.add(producto)
    db.session.commit()

    return producto_schema.dump(producto),201