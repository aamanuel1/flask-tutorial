import os

from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    if test_config is None:
        #load instance config if it exists
        app.config.from_pyfile('config.py', silent=True)
    else:
        #Otherwise load the test config that is passed into test_config
        app.config.from_mapping(test_config)

    #is instance folder there?
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #Hello world!
    @app.route('/hello')
    def hello():
        return 'Hello, World'
        
    #initialize the app with the init_app function.
    from . import db
    db.init_app(app)

    return app