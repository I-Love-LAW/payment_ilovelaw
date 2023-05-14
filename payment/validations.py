import jwt
from django.conf import settings


def cek_login(auth_header, username):
    try:
        list_auth_header = auth_header.split(' ')

        if list_auth_header[0] != 'Bearer':
            raise Exception("Token must start with Bearer")

        token = list_auth_header[1]
        payload = jwt.decode(jwt=token, key=str(settings.JWT_SECRET_KEY), algorithms=['HS512'], options={"verify_signature": False})
        username_token = payload['sub']

        return username == username_token
    except Exception as e:
        print(e)
        return False