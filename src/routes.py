from flask import Blueprint
from flask_graphql import GraphQLView

from controllers.jwt import createTokenController
from schema import schema

routes = Blueprint('routes', __name__)


@routes.route('/')
def index():
    return 'Python GraphQL API'


@routes.route('/api', methods=['POST'])
def api_key():
    return createTokenController()


routes.add_url_rule(
    '/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
