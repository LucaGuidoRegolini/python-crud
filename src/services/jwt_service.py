import datetime
import os
import jwt


class JwtService:

    @staticmethod
    def create_token():
        expiration = datetime.datetime.now(
            datetime.timezone.utc) + datetime.timedelta(minutes=60)
        payload = {
            'exp': expiration
        }

        secret = os.getenv('JWT_SECRET')
        token = jwt.encode(payload, secret, algorithm='HS256')

        return token if isinstance(token, str) else token.decode('utf-8')

    @staticmethod
    def decode_token(token):
        secret = os.getenv('JWT_SECRET')

        try:
            return jwt.decode(token, secret, algorithms=['HS256'])
        except jwt.exceptions.DecodeError:
            return None
