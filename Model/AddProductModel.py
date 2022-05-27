import pymongo
import random

class AddProductModel():
    def __init__(self):
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017")
        self.mydb = self.myclient["project"]
        self.mycollection = self.mydb["Product"]

    def add_data(self, data:dict):
        doc = self.mycollection.insert_one(data)

    def random_id(self):
        product_id = "C"
        for i in range (3):
            product_id +=str(random.randint(0,9))
        return product_id

    def create_id(self):
        while True:
            product_id = self.random_id()
            for i in (self.mycollection.find()):
                if product_id == i["_id"]:
                    break
            else:
                return product_id