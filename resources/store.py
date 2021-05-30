from flask_restful import Resource, reqparse
from models.store import StoreModel
from flask_jwt import jwt_required

class Store(Resource):

    @jwt_required()
    def get(self,name):
        store = StoreModel.find_store_by_name(name)
        if store:
            return store.json()
        else:
            return {"Message":f"Store {name} not found"}, 404

    @jwt_required()
    def post(self,name):
        store = StoreModel.find_store_by_name(name)
        if store:
            return {"Message": f"Store with name {name} already exists!"}
        
        store = StoreModel(name=name)
        store.save_to_db()
        return {"Message":f"Added store {name} to database."}, 201

    @jwt_required()
    def delete(self,name):
        store = StoreModel.find_store_by_name(name)
        if store:
            store.delete_from_db()
            return {"Message": f"Deleted store {name} from db"}, 201

        else:
            return {"Message":f"Store with name {name} doesn't exist."}, 201

class StoreList(Resource):

    @jwt_required()
    def get(self):
        return {"Stores" : [store.json() for store in StoreModel.query.all()]}