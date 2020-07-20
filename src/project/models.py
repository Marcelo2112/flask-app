from project import db, bcrypt

class Usuario(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String, nullable=False)
    password= db.Column(db.String, nullable=False)
    correo = db.Column(db.String, nullable=False)
    direccion = db.Column(db.String, nullable=True)

    def __init__(self, **kwargs):
        super(Usuario, self).__init__(**kwargs)
        self.password = self.generate_password_hash(**kwargs)

    def generate_password_hash(self,**kwargs):
        if 'password' in kwargs:
            return bcrypt.generate_password_hash(kwargs['password']).decode()

        return None

    #def __init__(self, nombre, password,confirmacion):
     #   self.nombre= nombre
      #  self.password= password

class Proveedor (db.Model):

    id_proveedor = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_empresa = db.Column(db.String, nullable=False)
    rut_empresa = db.Column(db.String, nullable=False)
    nombre_proveedor = db.Column(db.String, nullable=False)
    apellido_proveedor = db.Column(db.String, nullable=False)
    telefono_proveedor = db.Column(db.Integer, nullable=True)

class Insumo (db.Model):
    id_insumo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_insumo = db.Column(db.String, nullable=False)
    codigo_insumo = db.Column(db.Intenger, nuallable=False)
    cantidad_insumo = db.Column(db.Intenger, nuallable=False)
    color_insumo = db.Column(db.String, nuallable=True)
    medidas_insumo = db.Column(db.String, nuallable=True)
    marca_insumo = db.Column(db.String, nuallable=True)


