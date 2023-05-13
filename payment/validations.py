import jwt
from django.conf import settings

def cek_login(token, username):
    payload = jwt.decode(jwt=token, key=str(settings.JWT_SECRET_KEY), algorithms=['HS512'], options={"verify_signature": False})

    if username == payload['sub']:
        return True
    
    return False