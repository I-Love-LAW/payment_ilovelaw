import jwt

def cek_login(token, username):
    payload = jwt.decode(jwt=token, options={"verify_signature": False})

    if username == payload['sub']:
        return True
    
    return False