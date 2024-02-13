from flask import Flask
import os

# Application Factory Function

def create_app(testing=False):
    # Create the Flask application
    app = Flask(__name__)

    app.config['TESTING'] = testing

    register_blueprints(app)

    return app

def register_blueprints(app):
    # Since the application instance is now created, register each Blueprint
    # with the Flask application instance (app)
    from project.build_repo import build_repo_blueprint
    app.register_blueprint(build_repo_blueprint)
