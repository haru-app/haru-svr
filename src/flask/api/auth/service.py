from flask import jsonify
from src.database.database import Database
import jwt


class AuthService:
    def createAccessToken(self):
        data_to_encode = {"some": "payload"}
        encryption_secret = "secrete"
        algorithm = "HS256"
        encoded = jwt.encode(data_to_encode, encryption_secret, algorithm=algorithm)
        decoded = jwt.decode(encoded, encryption_secret, algorithms=[algorithm])
        print(decoded)


AuthService().createAccessToken()
