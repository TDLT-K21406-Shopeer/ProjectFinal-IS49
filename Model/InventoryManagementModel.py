from tkinter import *
from tkinter.ttk import Treeview
import pymongo

class InventoryManagementModel():
    def __init__(self):
        self.id = StringVar()
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017")
        self.mydb = self.myclient["project"]
        self.mycollection = self.mydb["Product"]
