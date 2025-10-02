from app import create_app
import os

app = create_app()

if __name__ == '__main__':
    # For development/testing only
    # In production, use: gunicorn -w 4 -b 0.0.0.0:5000 app:app
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '0.0.0.0')
    app.run(host=host, port=port, debug=False)