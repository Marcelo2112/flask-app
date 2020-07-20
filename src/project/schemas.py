from project import ma
from project.models import Usuario, Proveedor


class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Usuario
        load_instance = True  ##vi direccionalmente##
        load_only= ('password', )

#class EmpresaSchema(ma.SQLAlchemyAutoSchema):
 #   class Meta:
  #      model = Empresa 

class ProveedorSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = Proveedor
    load_instance = True

usuario_schema = UsuarioSchema()
proveedor_schema = ProveedorSchema()
#empresa_schema = EmpresaSchema()