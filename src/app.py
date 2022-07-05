from flask import Flask ,jsonify,request
from flask_cors import CORS

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app=Flask(__name__)
CORS(app)

# configuro la base de datos, con el nombre el usuario y la clave
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/flaskmysql'
#user:clave@localhost/nombreBaseDatos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db= SQLAlchemy(app)
ma=Marshmallow(app)

# defino la tabla
class Producto(db.Model):   # la clase Producto hereda de db.Model     
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    nombre=db.Column(db.String(100))
    precio=db.Column(db.Integer)
    stock=db.Column(db.Integer)
    imagen=db.Column(db.String(10000))
    autor=db.Column(db.String(255))
    fecha=db.Column(db.String(255))

    def __init__(self,nombre,precio,stock,imagen,autor,fecha):   #crea el  constructor de la clase
        self.nombre=nombre   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.precio=precio
        self.stock=stock
        self.imagen=imagen
        self.autor=autor
        self.fecha=fecha

db.create_all()  # crea las tablas
#  ************************************************************
class ProductoSchema(ma.Schema):
    class Meta:
        fields=('id','nombre','precio','stock','imagen','autor','fecha')

producto_schema=ProductoSchema()            # para crear un producto
productos_schema=ProductoSchema(many=True)  # multiples registros


@app.route('/productos',methods=['GET'])
def get_Productos():
    all_productos=Producto.query.all()     # query.all() lo hereda de db.Model
    result=productos_schema.dump(all_productos)  # .dump() lo hereda de ma.schema
    return jsonify(result)

@app.route('/productos/<id>',methods=['GET'])
def get_producto(id):
    producto=Producto.query.get(id)
    return producto_schema.jsonify(producto)

@app.route('/productos', methods=['POST']) # crea ruta o endpoint
def create_producto():
    print(request.json)  # request.json contiene el json que envio el cliente
    nombre=request.json['nombre']
    precio=request.json['precio']
    stock=request.json['stock']
    imagen=request.json['imagen']
    autor=request.json['autor']
    fecha=request.json['fecha']
    new_producto=Producto(nombre,precio,stock,imagen,autor,fecha)
    db.session.add(new_producto)
    db.session.commit()
    return producto_schema.jsonify(new_producto)

@app.route('/productos/<id>' ,methods=['PUT'])
def update_producto(id):
    producto=Producto.query.get(id)
   
    nombre=request.json['nombre']
    precio=request.json['precio']
    stock=request.json['stock']
    imagen=request.json['imagen']
    autor=request.json['autor']
    fecha=request.json['fecha']

    producto.nombre=nombre
    producto.precio=precio
    producto.stock=stock
    producto.imagen=imagen
    producto.autor=autor
    producto.fecha=fecha
    db.session.commit()
    return producto_schema.jsonify(producto)

@app.route('/producto/<id>',methods=['DELETE'])
def delete_producto(id):
    producto=Producto.query.get(id)
    db.session.delete(producto)
    db.session.commit()
    return producto_schema.jsonify(producto)


#TABLA CLIENTES
# defino la tabla
class Cliente(db.Model):   # la clase Producto hereda de db.Model     
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    nombre=db.Column(db.String(100))
    email=db.Column(db.String(100))
    telefono=db.Column(db.String(100))
    

    def __init__(self,nombre,email,telefono):   #crea el  constructor de la clase
        self.nombre=nombre   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.email=email
        self.telefono=telefono
        

db.create_all()  # crea las tablas
#  ************************************************************
class ClienteSchema(ma.Schema):
    class Meta:
        fields=('id','nombre','email','telefono')

cliente_schema=ClienteSchema()            # para crear un cliente
clientes_schema=ClienteSchema(many=True)  # multiples registros


@app.route('/clientes',methods=['GET'])
def get_Clientes():
    all_clientes=Cliente.query.all()     # query.all() lo hereda de db.Model
    result=clientes_schema.dump(all_clientes)  # .dump() lo hereda de ma.schema
    return jsonify(result)

@app.route('/clientes/<id>',methods=['GET'])
def get_cliente(id):
    cliente=Cliente.query.get(id)
    return cliente_schema.jsonify(cliente)

@app.route('/clientes', methods=['POST']) # crea ruta o endpoint
def create_cliente():
    print(request.json)  # request.json contiene el json que envio el cliente
    nombre=request.json['nombre']
    email=request.json['email']
    telefono=request.json['telefono']
    new_cliente=Cliente(nombre,email,telefono)
    db.session.add(new_cliente)
    db.session.commit()
    return producto_schema.jsonify(new_cliente)

@app.route('/clientes/<id>' ,methods=['PUT'])
def update_cliente(id):
    cliente=Cliente.query.get(id)
   
    nombre=request.json['nombre']
    email=request.json['email']
    telefono=request.json['telefono']
    

    cliente.nombre=nombre
    cliente.email=email
    cliente.telefono=telefono
    
    db.session.commit()
    return producto_schema.jsonify(cliente)

@app.route('/cliente/<id>',methods=['DELETE'])
def delete_cliente(id):
    cliente=Cliente.query.get(id)
    db.session.delete(cliente)
    db.session.commit()
    return cliente_schema.jsonify(cliente)


#TABLA PEDIDOS
# defino la tabla
class Pedido(db.Model):   # la clase Producto hereda de db.Model     
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    idCliente=db.Column(db.Integer)
    fecha=db.Column(db.String(30))
    monto=db.Column(db.String(100))
    direccionEntrega=db.Column(db.String(100))
    estado=db.Column(db.String(50))

    def __init__(self,idCliente,fecha,monto,direccionEntrega,estado):   #crea el  constructor de la clase
        self.idCliente=idCliente   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.fecha=fecha
        self.monto=monto
        self.direccionEntrega=direccionEntrega
        self.estado=estado

db.create_all()  # crea las tablas
#  ************************************************************
class PedidoSchema(ma.Schema):
    class Meta:
        fields=('id','idCliente','fecha','monto','direccionEntrega','estado')

pedido_schema=PedidoSchema()            # para crear un pedido
pedidos_schema=PedidoSchema(many=True)  # multiples registros


@app.route('/pedidos',methods=['GET'])
def get_Pedidos():
    all_pedidos=Pedido.query.all()     # query.all() lo hereda de db.Model
    result=pedidos_schema.dump(all_pedidos)  # .dump() lo hereda de ma.schema
    return jsonify(result)

@app.route('/pedidos/<id>',methods=['GET'])
def get_pedido(id):
    pedido=Pedido.query.get(id)
    return pedido_schema.jsonify(pedido) 

@app.route('/pedidos', methods=['POST']) # crea ruta o endpoint
def create_pedido():
    print(request.json)  # request.json contiene el json que envio el Cliente
    idCliente=request.json['idCliente']
    fecha=request.json['fecha']
    monto=request.json['monto']
    direccionEntrega=request.json['direccionEntrega']
    estado=request.json['estado']
    new_pedido=Pedido(idCliente,fecha,monto,direccionEntrega,estado)
    db.session.add(new_pedido)
    db.session.commit()
    return pedido_schema.jsonify(new_pedido)

@app.route('/pedidos/<id>' ,methods=['PUT'])
def update_pedido(id):
    pedido=Pedido.query.get(id)
   
    idCliente=request.json['idCliente']
    fecha=request.json['fecha']
    monto=request.json['monto']
    direccionEntrega=request.json['direccionEntrega']
    estado=request.json['estado']

    pedido.idCliente=idCliente
    pedido.fecha=fecha
    pedido.monto=monto
    pedido.direccionEntrega=direccionEntrega
    pedido.estado=estado

    db.session.commit()
    return pedido_schema.jsonify(pedido)

@app.route('/pedido/<id>',methods=['DELETE'])
def delete_pedido(id):
    pedido=Pedido.query.get(id)
    db.session.delete(pedido)
    db.session.commit()
    return pedido_schema.jsonify(pedido)


# TABLA DETALLE
class Detalle(db.Model):   # la clase Detalle hereda de db.Model     
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    idPedido=db.Column(db.Integer) 
    idProducto=db.Column(db.Integer) 
    precio=db.Column(db.Integer)
    cantidad=db.Column(db.Integer)


    def __init__(self,idPedido,idProducto,precio,cantidad):   #crea el  constructor de la clase
        self.idPedido=idPedido   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.idProducto=idProducto
        self.precio=precio
        self.cantidad=cantidad
        

db.create_all()  # crea las tablas
#  ************************************************************
class DetalleSchema(ma.Schema):
    class Meta:
        fields=('id','idPedido','idProducto','precio','cantidad')

detalle_schema=DetalleSchema()            # para crear un producto
detalles_schema=DetalleSchema(many=True)  # multiples registros


@app.route('/detalles',methods=['GET'])
def get_Detalles():
    all_detalles=Detalle.query.all()     # query.all() lo hereda de db.Model
    result=detalles_schema.dump(all_detalles)  # .dump() lo hereda de ma.schema
    return jsonify(result)

@app.route('/detalles/<id>',methods=['GET'])
def get_detalle(id):
    detalle=Detalle.query.get(id)
    return detalle_schema.jsonify(detalle)

@app.route('/detalles', methods=['POST']) # crea ruta o endpoint
def create_detalle():
    print(request.json)  # request.json contiene el json que envio el cliente
    idPedido=request.json['idPedido']
    idProducto=request.json['idProducto']
    precio=request.json['precio']
    cantidad=request.json['cantidad']
    new_detalle=Detalle(idPedido,idProducto,precio,cantidad)
    db.session.add(new_detalle)
    db.session.commit()
    return detalle_schema.jsonify(new_detalle)

@app.route('/detalles/<id>' ,methods=['PUT'])
def update_detalle(id):
    detalle=Detalle.query.get(id)
    idPedido=request.json['idPedido']
    idProducto=request.json['idProducto']
    precio=request.json['precio']
    cantidad=request.json['cantidad']

    detalle.idPedido=idPedido
    detalle.idProducto=idProducto
    detalle.precio=precio
    detalle.cantidad=cantidad
    db.session.commit()
    return detalle_schema.jsonify(detalle)

@app.route('/detalle/<id>',methods=['DELETE'])
def delete_detalle(id):
    detalle=Detalle.query.get(id)
    db.session.delete(detalle)
    db.session.commit()
    return detalle_schema.jsonify(detalle)


# programa principal
if __name__=='__main__':  
    app.run(debug=True, port=5000)  
