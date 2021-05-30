import sqlite3
from db import db

class ItemModel(db.Model):

    __tablename__ = "items"

    id = db.Column(db.Interger, primary_key=True)
    name = db.Column(db.String(50))
    price = db.Column(db.Float(precision=2))

    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def json(self):
        return {"name":self.name, "price":self.price}

    @classmethod
    def find_item_by_name(cls,name):
        conn = sqlite3.connect("./Section6/data.db")
        cursor = conn.cursor()

        query = "SELECT * FROM items WHERE name = ?"
        res = cursor.execute(query, (name,))
        row = res.fetchone()

        conn.close()

        if row:
            return cls(row[0], row[1])
        return None

    
    def insert(self):
        conn = sqlite3.connect("./Section6/data.db")
        cursor = conn.cursor()
        query = "INSERT INTO items VALUES (?, ?)"
        cursor.execute(query, (self.name, self.price))
        conn.commit()
        conn.close()

    def update(self):
        conn = sqlite3.connect("./Section6/data.db")
        cursor = conn.cursor()
        query = "UPDATE items SET price = ? where name = ?"
        cursor.execute(query, (self.price,self.name))
        conn.commit()
        conn.close()