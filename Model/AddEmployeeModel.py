import pymongo

class AddEmployeeModel():
    def __init__(self):
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.myclient["project"]
        self.mycollection_emp= self.mydb["Employee"]
        self.mycollection_adm= self.mydb["Admin"]

    def add_data(self,data:dict, col):
        doc = col.insert_one(data)
    
    def create_id(self,role):
        if role == "Admin":
            id="c"
        else:
            id ="e"
        count_doc =str(self.mycollection_emp.count_documents({})+1)
        count_doc = (3-len(count_doc))*"0"+count_doc
        return id+count_doc
