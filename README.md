# Solar Energy Management API

![Deployment Status](https://github.com/Yullianka/database_labs/actions/workflows/deploy.yml/badge.svg)
[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.1.2-green.svg)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://docker.com)
[![AWS](https://img.shields.io/badge/AWS-EC2%20%2B%20RDS-orange.svg)](https://aws.amazon.com)

## 🌟 Overview

REST API для системи управління сонячною енергією з повною Swagger документацією та автоматичним deployment.

## 🚀 Live Demo

- **Application:** http://98.88.76.225:5000/
- **Swagger Documentation:** http://98.88.76.225:5000/swagger/

## 📁 Project Structure

```
mybd/
├── app/                    # Flask application
│   ├── controller/         # Business logic controllers
│   ├── dao/               # Data access objects
│   ├── domain/            # Domain models
│   ├── root/              # API routes with Swagger docs
│   └── service/           # Service layer
├── .github/workflows/     # CI/CD automation
├── docker-compose.yml     # Container orchestration
└── requirements.txt       # Python dependencies
```

## 🛠 Technologies

- **Backend:** Flask 3.1.2, SQLAlchemy
- **Database:** AWS RDS MySQL
- **Documentation:** Swagger/OpenAPI (Flasgger)
- **Deployment:** Docker, AWS EC2
- **CI/CD:** GitHub Actions

## 📚 API Documentation

Система надає 60+ REST endpoints для управління:
- 👥 Користувачами
- ☀️ Сонячними станціями
- 🔋 Батареями та зарядами
- 📊 Продажами енергії
- 🏠 Домогосподарствами
- 📐 Панелями та кутами нахилу

## 🔄 Continuous Deployment

Автоматичний deployment при push в гілку `lab4`:
1. GitHub Actions підключається до AWS EC2
2. Виконує git pull та rebuild контейнерів
3. Запускає health checks
4. Підтверджує успішний deployment