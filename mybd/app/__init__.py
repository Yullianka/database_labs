import mysql.connector
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from app.root import register_routes
import os
from app.database import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    register_routes(app)

    create_database()
    print("База даних створена.")
    
    db.init_app(app)
    
    with app.app_context():
        create_tables(app) 
        print("Таблиці даних створені.")
        populate_data()  
    
    return app

def create_database():
    try:
        connection = mysql.connector.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            port=Config.DB_PORT,
        )
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {Config.DB_NAME}")
        cursor.close()
        connection.close()
        print(f"Database '{Config.DB_NAME}' created successfully.")
    except mysql.connector.Error as error:
        if "database exists" in str(error).lower():
            print(f"Database '{Config.DB_NAME}' already exists.")
        else:
            print(f"Error creating database: {error}")

def create_tables(app):
    with app.app_context():  
        db.create_all()

def populate_data():
    sql_file_path = os.path.abspath('data.sql')
    if os.path.exists(sql_file_path):
        connection = mysql.connector.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME,
            port=Config.DB_PORT,
        )
        cursor = connection.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM billing_account")
        count = cursor.fetchone()[0]
        
        if count > 0:
            print("Дані вже існують в базі даних. Пропуск заповнення.")
            cursor.close()
            connection.close()
            return
        
        print("Заповнення бази даних тестовими даними...")
        with open(sql_file_path, 'r') as sql_file:
            sql_text = sql_file.read()
            sql_statements = sql_text.split(';')
            for statement in sql_statements:
                statement = statement.strip()
                if statement:
                    try:
                        cursor.execute(statement)
                        connection.commit()
                    except mysql.connector.Error as error:
                        print(f"Error executing SQL statement: {error}")
                        print(f"SQL statement: {statement}")
                        connection.rollback()
        print("Тестові дані успішно додані до бази даних.")
        cursor.close()
        connection.close()

app = create_app()