import time
import jwt

# 设置密钥
SECRET_KEY = 'naxx1426'


# 创建新的JWT令牌的函数
def create_jwt(payload, expiration_seconds=3600):
    # 设置令牌的过期时间
    payload['exp'] = int(time.time()) + expiration_seconds
    # 将载荷和密钥编码生成新的令牌
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token


# 验证JWT令牌的函数
def verify_jwt(token):
    try:
        # 使用密钥解码令牌
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        # 如果解码成功，则返回True和解码后的令牌
        return True, decoded
    except jwt.ExpiredSignatureError:
        # 如果令牌已过期，则返回False和一个错误消息
        return False, 'Token已过期'
    except jwt.InvalidTokenError:
        # 如果令牌无效，则返回False和一个错误消息
        return False, '无效的Token'


# 刷新JWT令牌的函数
def refresh_jwt(token):
    try:
        # 使用密钥解码令牌，并在不验证过期时间的情况下创建新的令牌
        decoded = jwt.decode(token, SECRET_KEY, options={"verify_exp": False})
        new_token = create_jwt(decoded)
        # 如果刷新令牌成功，则返回True和新的令牌
        return True, new_token
    except jwt.InvalidTokenError:
        # 如果令牌无效，则返回False和一个错误消息
        return False, '无效的Token'
