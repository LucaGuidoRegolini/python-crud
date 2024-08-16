from flask import Flask
from models import register_models
from schema import register_schema

app = Flask(__name__)

if __name__ == '__main__':
    with app.app_context():
        register_models(app)
        register_schema(app)
    app.run(debug=True)
