from app.models import Usuario
from flask import jsonify, request

def index():
    response = {}
    return jsonify(response)

# Traer todos los usuarios
def get_all_usuarios():
    usuarios = Usuario.get_all()
    return jsonify([usuario.serialize() for usuario in usuarios])

# Traer un usuario por id
def get_usuario(usuario_id):
    usuario = Usuario.get_by_id(usuario_id)
    if not usuario:
        return jsonify({'message': 'Usuario not found'}), 404
    return jsonify(usuario.serialize())



# Traer un usuario por nombre

def get_usuarios_por_nombre():
    nombre = request.args.get('nombre', '')
    if not nombre:
        return jsonify({'message': 'Nombre is required'}), 400

    usuarios = Usuario.get_by_nombre(nombre)
    if not usuarios:
        return jsonify({'message': 'No users found'}), 404

    return jsonify([usuario.serialize() for usuario in usuarios])



# Crear un usuario
def create_usuario():
    data = request.json
    new_usuario = Usuario(
        apellido=data['apellido'], nombre=data['nombre'],
        fecha_nacimiento=data['fecha_nacimiento'], documento=data['documento'],
        telefono=data['telefono'], email=data['email'], pais_origen=data['pais_origen'],
        password=data['password']
    )
    new_usuario.save()
    return jsonify({'message': 'Usuario created successfully'}), 201

# Actualizar usuario
def update_usuario(usuario_id):
    usuario = Usuario.get_by_id(usuario_id)
    if not usuario:
        return jsonify({'message': 'Usuario not found'}), 404
    data = request.json
    usuario.apellido = data['apellido']
    usuario.nombre = data['nombre']
    usuario.fecha_nacimiento = data['fecha_nacimiento']
    usuario.documento = data['documento']
    usuario.telefono = data['telefono']
    usuario.email = data['email']
    usuario.pais_origen = data['pais_origen']
    usuario.password = data['password']
    usuario.save()
    return jsonify({'message': 'Usuario updated successfully'})

# Eliminar un usuario
def delete_usuario(usuario_id):
    usuario = Usuario.get_by_id(usuario_id)
    if not usuario:
        return jsonify({'message': 'Usuario not found'}), 404
    usuario.delete()
    return jsonify({'message': 'Usuario deleted successfully'})


# Buscar usuarios por nombre y/o documento
def search_usuarios():
    nombre = request.args.get('nombre')
    documento = request.args.get('documento')

    usuarios = Usuario.search(nombre=nombre, documento=documento)
    if not usuarios:
        return jsonify({'message': 'No users found'}), 404

    return jsonify([usuario.serialize() for usuario in usuarios])
