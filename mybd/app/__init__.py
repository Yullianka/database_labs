import psycopg2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from app.root import register_routes
import os
from app.database import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)  

    
    register_routes(app)

    
    with app.app_context():
        create_database()  
        create_tables(app) 
        print("Таблиці даних створені.")
        populate_data()  
    
    return app

def create_database():
    try:
        connection = psycopg2.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            port=Config.DB_PORT,
        )
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE {Config.DB_NAME}")
        cursor.close()
        connection.close()
        print(f"Database '{Config.DB_NAME}' created successfully.")
    except psycopg2.errors.DuplicateDatabase:
        print(f"Database '{Config.DB_NAME}' already exists.")
    except Exception as e:
        print(f"Error creating database: {e}")

def create_tables(app):
    with app.app_context():  
        db.create_all()

def populate_data():
    sql_file_path = os.path.abspath('data.sql')
    if os.path.exists(sql_file_path):
        connection = psycopg2.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME,
            port=Config.DB_PORT,
        )
        cursor = connection.cursor()
        with open(sql_file_path, 'r') as sql_file:
            sql_text = sql_file.read()
            sql_statements = sql_text.split(';')
            for statement in sql_statements:
                statement = statement.strip()
                if statement:
                    try:
                        cursor.execute(statement)
                        connection.commit()
                    except psycopg2.Error as error:
                        print(f"Error executing SQL statement: {error}")
                        print(f"SQL statement: {statement}")
                        connection.rollback()
        cursor.close()
        connection.close()

# Create the app instance for Gunicorn
app = create_app()