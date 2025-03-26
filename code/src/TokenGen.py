import jwt
token = jwt.encode({"role": "admin"}, "your_secret_key", algorithm="HS256")
print(token)
