import os
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flasgger import Swagger

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database import db
from app.root import register_routes

def create_local_app():
    app = Flask(__name__)
    
    # Local configuration for testing
    app.config['SECRET_KEY'] = 'local-dev-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///local_solar.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Enable CORS for all routes
    CORS(app)
    
    # Configure Swagger
    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec_1',
                "route": '/apispec_1.json',
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/swagger/",
        "title": "Solar Energy Management API",
        "version": "1.0.0",
        "description": "REST API для системи управління сонячною енергією (Local Development)",
    }
    
    swagger = Swagger(app, config=swagger_config)
    
    # Initialize database
    db.init_app(app)
    
    # Register routes
    register_routes(app)
    
    # Add Flask-RESTX API documentation
    try:
        from app.swagger_config import api_blueprint
        from app import api_routes
        app.register_blueprint(api_blueprint)
    except ImportError as e:
        print(f"Warning: Could not import Flask-RESTX routes: {e}")
    
    # Register main page route
    try:
        from app.root.main_route import main_bp
        app.register_blueprint(main_bp)
    except ImportError as e:
        print(f"Warning: Could not import main route: {e}")
    
    # Create tables for local testing
    with app.app_context():
        try:
            db.create_all()
            print("Local SQLite database tables created successfully.")
        except Exception as e:
            print(f"Error creating tables: {e}")
    
    return app

if __name__ == '__main__':
    app = create_local_app()
    print("Starting Flask application on http://localhost:5000")
    print("Swagger UI available at: http://localhost:5000/swagger/")
    print("API Documentation available at: http://localhost:5000/api/doc/")
    app.run(host='0.0.0.0', port=5000, debug=True)
