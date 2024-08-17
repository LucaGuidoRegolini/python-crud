from flask import Blueprint

from controllers.jwt import createTokenController

routes = Blueprint('routes', __name__)


@routes.route('/api', methods=['POST'])
def api_key():
    return createTokenController()
