from flask import Flask

from database import db
from views import blueprints


def create_app(debug=False):
    app = Flask(__name__)
    app.config['WTF_CSRF_SECRET_KEY'] = 'A SECRET KEY'
    app.config['SECRET_KEY'] = 'ANOTHER ONE'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storytellers.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # DEBUGGING AND TESTING
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['TESTING'] = debug
    app.config['LOGIN_DISABLED'] = not debug
    app.config['WTF_CSRF_ENABLED'] = debug

    for bp in blueprints:
        app.register_blueprint(bp)
        bp.app = app

    db.init_app(app)
    db.create_all(app=app)
    return app


if __name__ == '__main__':

    app = create_app()
    app.run()
