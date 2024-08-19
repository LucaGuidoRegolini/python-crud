import os
from flask import Flask
from dotenv import load_dotenv
from models import register_models
import routes

app = Flask(__name__)

load_dotenv()
with app.app_context():
    register_models(app)
    app.register_blueprint(routes.routes)

debug = os.getenv('DEBUG_MODE')

if __name__ == '__main__':
    app.run(debug=debug, host='0.0.0.0')
