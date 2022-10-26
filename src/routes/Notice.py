from flask import Blueprint, jsonify, request
import uuid

# Entities
from models.entities.Notice import Notice

# Models
from models.NoticeModels import NoticeModel


main = Blueprint('notice_blueprint', __name__)


@main.route('/add', methods=['POST'])
def add_notice():
    try:
        title = request.json['Título']
        description = request.json['Descripción']
        id = uuid.uuid4()
        notice = Notice(str(id),title, description)

        affected_rows = NoticeModel.add_notice(notice)

        if affected_rows == 1:
            return jsonify({'Message': 'Noticia creada correctamente'})
        else:
            return jsonify({'Message': "Error al crear la noticia"}), 500

    except Exception as e:
        return jsonify({'Message': str(e)}), 500


@main.route('/<id>')
def get_notice(id):
    try:
        notice = NoticeModel.get_notice(id)
        if notice != None:
            return jsonify(notice)
        else:
            return jsonify({'Message': 'Noticia no encontrada'}), 404
    except Exception as e:
        return jsonify({'Message': str(e)}), 500


@main.route('/')
def get_notices():
    try:
        notices = NoticeModel.get_notices()
        return jsonify(notices)
    except Exception as e:
        return jsonify({"Message": str(e)}), 404


@main.route('/update/<id>', methods=['PUT'])
def update_notice(id):
    try:
        title = request.json['Título']
        description = request.json['Descripción']
        notice = Notice(id, title, description)

        affected_rows = NoticeModel.update_notice(notice)

        if affected_rows == 1:
            return jsonify({'Message': 'La noticia fue actualizada'})
        else:
            return jsonify({'Message': 'Noticia no actualizada'}), 404

    except Exception as e:
        return jsonify({'Message': str(e)}), 500


@main.route('/delete/<id>', methods=['DELETE'])
def delete_notice(id):
    try:
        notice = Notice(id)

        affected_rows = NoticeModel.delete_notice(notice)

        if affected_rows == 1:
            return jsonify(notice.id)
        else:
            return jsonify({'message': "No se eliminó la noticia"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
