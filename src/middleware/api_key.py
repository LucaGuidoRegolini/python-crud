from functools import wraps
from flask import request
from graphql import GraphQLError

from services.jwt_service import JwtService


def api_key_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        bear_token = request.headers.get('Authorization')

        if not bear_token or not bear_token.startswith('Bearer '):
            raise GraphQLError("Invalid API Key or Key not provided!")

        api_key = bear_token.replace('Bearer ', '') if bear_token else None
        token = JwtService.decode_token(api_key)

        if not token:
            raise GraphQLError("Invalid API Key or Key not provided!")
        return f(*args, **kwargs)
    return decorated
