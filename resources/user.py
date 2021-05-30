import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True, help="Username cannot be blank")
    parser.add_argument("password", type=str, required=True, help="Password cannot be blank")

    def post(self):

        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data["username"]):
            return {"Message":"User already exists!"}, 400

        #user = UserModel(data["username"], data["password"])
        user = UserModel(data["username"], data["password"])
        user.save_to_db()

        return {"Message":f"User '{data['username']}' created successfully."}