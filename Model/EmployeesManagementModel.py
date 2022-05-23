from tkinter import *
from tkinter.ttk import *
import pymongo

class EmployeesManagementModel():
    def __init__(self):
        self.id = StringVar()
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017")
        self.mydb = self.myclient["project"]
        self.mycollection_emp = self.mydb["Employee"]
        self.mycollection_adm = self.mydb["Admin"]