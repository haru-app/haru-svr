from flask import jsonify
from src.database.database import Database


class UserService:
    def getUser(self):
        data = Database.query('SELECT * FROM "user"').all()
        return jsonify(data)
