import pymongo

class UpdateEmployeeModel():
    def __init__(self):
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.myclient["project"]
        self.mycollection_emp= self.mydb["Employee"]
        self.mycollection_adm= self.mydb["Admin"]

    def update(self,data:dict,col,val):
        col.update_one({"_username":val},{"$set":data})