from tkinter import StringVar, messagebox
import pymongo

class AddProductModel():
    def __init__(self):
        self.name = StringVar()
        self.quantity = StringVar()
        self.price_in = StringVar()
        self.price_out = StringVar()
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017")
        self.mydb = self.myclient["project"]
        self.mycollection = self.mydb["Product"]

    def check_quantity(self):
        quantity = self.quantity.get()
        if quantity.isdigit():
            return True
        else:
            messagebox.showerror("Error", "Quantity is an integer number")
        return False

    def check_price(self):
        price_in = self.price_in.get()
        price_out = self.price_out.get()
        if price_in.isdigit():
            if price_out.isdigit():
                return True
            else:
                messagebox.showerror("Error","Price out is an integer value")
        else:
            messagebox.showerror("Error","Price in is an integer value") 
        return False