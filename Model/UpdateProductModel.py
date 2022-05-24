import pymongo

class UpdateProductModel():
    def __init__(self):
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.myclient["project"]
        self.mycollection =self.mydb["Product"]

    def update(self,data:dict,val):
        self.mycollection.update_one({"car_name":val},{"$set":data})