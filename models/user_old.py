import sqlite3
from db import db

class UserModel(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))

    def __init__(self,_id,username,password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls,username):
        conn = sqlite3.connect("./Section6/data.db")
        cursor = conn.cursor()

        query = "SELECT * FROM users WHERE username = ?"
        res = cursor.execute(query, (username,))
        row = res.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        conn.close()
        return user

    @classmethod
    def find_by_id(cls,_id):
        conn = sqlite3.connect("./Section6/data.db")
        cursor = conn.cursor()

        query = "SELECT * FROM users WHERE id = ?"
        res = cursor.execute(query, (_id,))
        row = res.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        conn.close()
        return user