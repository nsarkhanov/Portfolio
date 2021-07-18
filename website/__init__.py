from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'aksakhfkjhakfjhaksf'
    from .views import pages
    from .auth import auth

    app.register_blueprint(pages, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app
