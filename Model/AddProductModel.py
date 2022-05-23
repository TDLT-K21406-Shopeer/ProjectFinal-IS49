import pymongo

class AddProductModel():
    def __init__(self):
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017")
        self.mydb = self.myclient["project"]
        self.mycollection = self.mydb["Product"]

    def add_data(self, data:dict):
        doc = self.mycollection.insert_one(data)

    def create_id(self):
        count_doc = str(100+self.mycollection.count_documents({})+1)
        count_doc = (3-len(count_doc))*"0"+count_doc
        return "C"+count_doc