from flask import Flask
from dotenv import load_dotenv
from models import register_models
import routes
from schema import register_schema

app = Flask(__name__)


@app.route('/')
def index():
    return 'Python GraphQL API'


app.register_blueprint(routes.routes)


if __name__ == '__main__':
    load_dotenv()

    with app.app_context():
        register_models(app)
        register_schema(app)
    app.run(debug=True)
