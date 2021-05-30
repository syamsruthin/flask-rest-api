from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

import sqlite3

from models.item import ItemModel

class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
            type = float,
            required = True,
            help = "Cannot leave price as blank."
        )
    parser.add_argument('store_id',
            type = int,
            required = True,
            help = "Cannot leave store_id as blank."
        )

    
    @jwt_required()
    def get(self,name):
        item = ItemModel.find_item_by_name(name)
        if item:
            return item.json()
        return {"Message":"Item not found in database."}, 404

    @jwt_required()
    def post(self,name):
        #if next(filter(lambda x : x["name"] == name, items)) is not None:
        item = ItemModel.find_item_by_name(name)
        if item:
            return {"Messgae":f"Item with name '{name}' already exists."}, 400

        #data = request.get_json()
        data = Item.parser.parse_args()

        new_item = ItemModel(name, data["price"], data["store_id"])
        try:       
            new_item.save_to_db()
        except:
            return {"Message": "Error occurred while inserting item to database."}, 500

        return {"Message: ": "Added item to the list."}, 201

    @jwt_required()
    def delete(self,name):
        item = ItemModel.find_item_by_name(name)
        if item:
            item.delete_from_db()
            return {"Message":f"Item '{name}' deleted."}, 201

        else:
            return {"Message":f"Item '{name}' not found."}, 201

    @jwt_required()
    def put(self,name):
        
        data = Item.parser.parse_args()

        item = ItemModel.find_item_by_name(name)
        
        if item is None:                        
            item = ItemModel(name,data["price"], data["store_id"])
           
        else:
            item.price = data["price"]
            item.store_id = data["store_id"]

        item.save_to_db()
            
        return item.json()


class ItemList(Resource):
    @jwt_required()
    def get(self):
        return {"items": [item.json() for item in ItemModel.query.all()]}