from flask import jsonify
from services.jwt_service import JwtService


def createTokenController():
    token = JwtService.create_token()
    return jsonify({'token': token})
