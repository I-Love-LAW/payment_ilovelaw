import jwt, base64
from django.conf import settings

def cek_login(token, username):
    payload = jwt.decode(jwt=token, options={"verify_signature": False})
    print(payload)
    payload = jwt.decode(jwt=token, key=str(settings.JWT_SECRET_KEY), algorithms=['HS512'], options={"verify_signature": False})
    print(payload)

    try:
        payload = jwt.decode(jwt=token, key=base64.b64decode(settings.JWT_SECRET_KEY), algorithms=['HS256'])
    except Exception as e:
        print(1)
        print(e)

    try:
        payload = jwt.decode(jwt=token, key=base64.b64decode(settings.JWT_SECRET_KEY), algorithms=['HS512'])
    except Exception as e:
        print(2)
        print(e)

    try:
        payload = jwt.decode(jwt=token, key=base64.b32decode(settings.JWT_SECRET_KEY), algorithms=['HS256'])
    except Exception as e:
        print(3)
        print(e)

    try:
        payload = jwt.decode(jwt=token, key=base64.b32decode(settings.JWT_SECRET_KEY), algorithms=['HS512'])
    except Exception as e:
        print(4)
        print(e)

    try:
        payload = jwt.decode(jwt=token, key=base64.standard_b64decode(settings.JWT_SECRET_KEY), algorithms=['HS256'])
    except Exception as e:
        print(5)
        print(e)

    try:
        payload = jwt.decode(jwt=token, key=base64.standard_b64decode(settings.JWT_SECRET_KEY), algorithms=['HS512'])
    except Exception as e:
        print(6)
        print(e)

    try:
        payload = jwt.decode(jwt=token, key=settings.JWT_SECRET_KEY, algorithms=['HS256'])
    except Exception as e:
        print(7)
        print(e)

    try:
        payload = jwt.decode(jwt=token, key=settings.JWT_SECRET_KEY, algorithms=['HS512'])
    except Exception as e:
        print(8)
        print(e)

    try:
        payload = jwt.decode(jwt=token, key=str(settings.JWT_SECRET_KEY), algorithms=['HS256'])
    except Exception as e:
        print(9)
        print(e)

    try:
        payload = jwt.decode(jwt=token, key=str(settings.JWT_SECRET_KEY), algorithms=['HS512'])
    except Exception as e:
        print(10)
        print(e)

    if username == payload['sub']:
        return True
    
    return False