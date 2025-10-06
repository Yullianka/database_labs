from flask import Blueprint, render_template_string

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    html_template = """
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Solar Energy Management System</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 30px;
        }
        .header h1 {
            margin: 0;
            font-size: 2.5em;
        }
        .header p {
            margin: 10px 0 0 0;
            font-size: 1.2em;
            opacity: 0.9;
        }
        .content {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .api-section {
            margin-bottom: 30px;
        }
        .api-section h2 {
            color: #333;
            border-bottom: 2px solid #667eea;
            padding-bottom: 10px;
        }
        .endpoint-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }
        .endpoint-card {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 8px;
            border-left: 4px solid #667eea;
        }
        .endpoint-card h3 {
            margin: 0 0 10px 0;
            color: #333;
        }
        .endpoint-card p {
            margin: 5px 0;
            color: #666;
        }
        .method {
            display: inline-block;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.8em;
            font-weight: bold;
            margin-right: 10px;
        }
        .method.get { background: #28a745; color: white; }
        .method.post { background: #007bff; color: white; }
        .method.put { background: #ffc107; color: black; }
        .method.delete { background: #dc3545; color: white; }
        .swagger-link {
            background: #17a2b8;
            color: white;
            padding: 15px 30px;
            text-decoration: none;
            border-radius: 5px;
            display: inline-block;
            margin: 20px 0;
            font-weight: bold;
            transition: background 0.3s;
        }
        .swagger-link:hover {
            background: #138496;
            text-decoration: none;
            color: white;
        }
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }
        .stat-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
        }
        .stat-card h3 {
            margin: 0;
            font-size: 2em;
        }
        .stat-card p {
            margin: 5px 0 0 0;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🌞 Solar Energy Management System</h1>
        <p>REST API для системи управління сонячною енергією</p>
    </div>

    <div class="content">
        <div class="api-section">
            <h2>📚 API Документація</h2>
            <p>Система надає повний REST API для управління сонячними станціями, користувачами, батареями та продажами енергії.</p>
            
            <a href="/swagger/" class="swagger-link">
                📖 Відкрити Swagger UI Documentation
            </a>
        </div>

        <div class="stats">
            <div class="stat-card">
                <h3>20+</h3>
                <p>REST Endpoints</p>
            </div>
            <div class="stat-card">
                <h3>5</h3>
                <p>Основних модулів</p>
            </div>
            <div class="stat-card">
                <h3>AWS</h3>
                <p>RDS MySQL</p>
            </div>
            <div class="stat-card">
                <h3>Docker</h3>
                <p>Containerized</p>
            </div>
        </div>

        <div class="api-section">
            <h2>🔗 Доступні API Endpoints</h2>
            
            <div class="endpoint-grid">
                <div class="endpoint-card">
                    <h3>👥 Users</h3>
                    <p><span class="method get">GET</span> /api/users/ - Список користувачів</p>
                    <p><span class="method post">POST</span> /api/users/ - Створити користувача</p>
                    <p><span class="method get">GET</span> /api/users/{id} - Отримати користувача</p>
                    <p><span class="method put">PUT</span> /api/users/{id} - Оновити користувача</p>
                    <p><span class="method delete">DELETE</span> /api/users/{id} - Видалити користувача</p>
                </div>

                <div class="endpoint-card">
                    <h3>🌞 Solar Stations</h3>
                    <p><span class="method get">GET</span> /api/solar-stations/ - Список станцій</p>
                    <p><span class="method post">POST</span> /api/solar-stations/ - Створити станцію</p>
                    <p><span class="method get">GET</span> /api/solar-stations/{id} - Отримати станцію</p>
                </div>

                <div class="endpoint-card">
                    <h3>🔋 Batteries</h3>
                    <p><span class="method get">GET</span> /api/batteries/ - Список батарей</p>
                    <p>Моніторинг та управління батареями</p>
                </div>

                <div class="endpoint-card">
                    <h3>💰 Energy Sales</h3>
                    <p><span class="method get">GET</span> /api/energy-sales/ - Продажі енергії</p>
                    <p>Відстеження продажів та доходів</p>
                </div>

                <div class="endpoint-card">
                    <h3>💳 Billing</h3>
                    <p><span class="method get">GET</span> /api/billing/ - Рахунки</p>
                    <p><span class="method get">GET</span> /api/billing/{id} - Деталі рахунку</p>
                </div>

                <div class="endpoint-card">
                    <h3>🏠 Traditional Routes</h3>
                    <p>Традиційні Flask routes також доступні</p>
                    <p>Для веб-інтерфейсу та HTML сторінок</p>
                </div>
            </div>
        </div>

        <div class="api-section">
            <h2>🛠 Технології</h2>
            <ul>
                <li><strong>Backend:</strong> Flask + SQLAlchemy</li>
                <li><strong>API:</strong> Flask-RESTX (Swagger)</li>
                <li><strong>Database:</strong> AWS RDS MySQL</li>
                <li><strong>Deployment:</strong> Docker + AWS EC2</li>
                <li><strong>Documentation:</strong> Swagger UI</li>
            </ul>
        </div>
    </div>
</body>
</html>
    """
    return render_template_string(html_template)
