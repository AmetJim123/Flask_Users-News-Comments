from flask import Flask

from config import config

# ROUTES
from routes import User, Notice, Comment


app = Flask(__name__)


def page_not_found(error):
    return "<h1>Page not found</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(User.main, url_prefix='/api/users')
    app.register_blueprint(Comment.main, url_prefix='/api/comments')
    app.register_blueprint(Notice.main, url_prefix='/api/notices')


    # Error Handler
    app.register_error_handler(404, page_not_found)

    app.run()
