from flask import Blueprint, jsonify, request
import uuid

#Entities
from models.entities.User import User

# Models
from models.UserModels import UserModel


main = Blueprint('user_blueprint', __name__)


@main.route('/')
def get_users():
    try:
        users = UserModel.get_users()
        return jsonify(users)
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@main.route('/add', methods=['POST'])
def add_user():
    try:
        id = uuid.uuid4()
        full_name = request.json['Nombre Completo']
        email = request.json['Correo']
        password = request.json['Contraseña']
        address = request.json['Dirección']
        phone = int(request.json['Teléfono'])
        birthdate = request.json['Fecha de Nacimiento']

        user = User(str(id), full_name, email, password, address, phone, birthdate)

        affected_rows = UserModel.add_user(user)

        if affected_rows == 1:
            return jsonify(user.id)
        else:
            return jsonify({'Message': "Error al crear usuario"}), 500

    except Exception as e:
        return jsonify({'Message': str(e)}), 500


@main.route('/<email>&<password>')
def get_user(email, password):
    try:
        user = UserModel.get_user(email,password)
        if user != None:
            return jsonify({'Message': 'Usuario y contraseña correctos'})
        else:
            return jsonify({'Message' : 'Usuario y contraseña incorrectos'}),404
    except Exception as e:
        return jsonify({'Message': str(e)}), 500
