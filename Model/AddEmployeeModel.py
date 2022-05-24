import pymongo
import random

class AddEmployeeModel():
    def __init__(self):
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.myclient["project"]
        self.mycollection_emp= self.mydb["Employee"]
        self.mycollection_adm= self.mydb["Admin"]

    def add_data(self,data:dict, col):
        doc = col.insert_one(data)
    
    def random_id(self):
        product_id=""
        for i in range (3):
            product_id +=str(random.randint(0,9))
        return product_id

    def create_id(self,role):
        if role == "Admin":
            while True:
                id="c"+ self.random_id()
                for data in (self.mycollection_emp.find()):
                    if data["_id"]==id:
                        break
                else:
                    return id
        else:
            while True:
                id ="e"+self.random_id()
                for data in (self.mycollection_emp.find()):
                    if data["_id"]==id:
                        break
                else:
                    return id
        
