from project import ma
from project.models import Usuario, Proveedor, Insumo


class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Usuario
        load_instance = True  ##vi direccionalmente##
        load_only= ('password', )

class ProveedorSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = Proveedor
    load_instance = True

class InsumoSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = Insumo
    load_instance = True

usuario_schema = UsuarioSchema()
proveedor_schema = ProveedorSchema()
insumo_schema = InsumoSchema()
