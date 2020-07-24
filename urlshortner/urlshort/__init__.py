from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

    from . import urlshort
    app.register_blueprint(urlshort.bp)

    return app