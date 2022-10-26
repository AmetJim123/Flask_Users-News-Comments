from flask import Blueprint, jsonify, request

# Entities
from models.entities.Comment import Comment, FullNotice

# Models
from models.CommentModels import CommentModels

main = Blueprint('comment_blueprint', __name__)

@main.route('/add', methods=['POST'])
def add_comment():
    try:
        id = request.json['ID']
        comment = request.json['Comentario']

        commentary = Comment(id, comment)

        affected_rows = CommentModels.add_comment(commentary)

        if affected_rows == 1:
            return jsonify({'Message': 'Se ha subido su comentario'})
        else:
            return jsonify({'Message': 'Error al subir comentario'}), 500
        
    except Exception as e:
        return jsonify({'Message': str(e)}), 500


@main.route('/')
def get_comments():
    try:
        comments = CommentModels.get_comments()
        return jsonify(comments)
    except Exception as e:
        return jsonify({'Message': str(e)}), 500