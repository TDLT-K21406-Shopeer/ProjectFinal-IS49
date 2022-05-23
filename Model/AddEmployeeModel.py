import random
from tkinter import StringVar, messagebox
import pymongo

class AddEmployeeModel():
    def __init__(self):
        self.name = StringVar()
        self.phone_sub = StringVar()
        self.role = StringVar()
        self.age = StringVar()
        self.wage = StringVar()
        self.phone = StringVar()
        self.username = StringVar()
        self.password = StringVar()
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.myclient["project"]
        self.mycollection_emp= self.mydb["Employee"]
        self.mycollection_adm= self.mydb["Admin"]

    def add_data(self,data:dict, col):
        doc = col.insert_one(data)
    
    def random_id(self,role):
        if role == "Admin":
            id="c"
        else:
            id ="e"
        for i in range(3):
            id += str(random.randint(0,10))
        return id