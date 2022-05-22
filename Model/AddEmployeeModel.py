from tkinter import StringVar, messagebox
import pymongo

class AddEmployeeModel():
    def __init__(self):
        self.name = StringVar()
        self.age = StringVar()
        self.wage = StringVar()
        self.phone = StringVar()
        self.username = StringVar()
        self.password = StringVar()
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.myclient["project"]
        self.mycollection = self.mydb["Employee"]

    def check_phone(self):
        phone = self.phone.get()
        if  phone.isdigit():
            if len(phone) ==10:
                if phone.startwith("0"):
                    return True
                else:
                    messagebox.showerror("Error","Phone number does not exist")
            else:
                messagebox.showerror("Error","Phone number does not exist")
        else:
            messagebox.showerror("Error", "Phone numbers only include numbers")
        return False

    def check_age(self):
        age = self.age.get()
        if age.isdigit():
            if int(age)>=18 and int(age)<=60:
                return True
            else:
                messagebox.showerror("Error","Employee of working age is 18 to 60")
        else:
            messagebox.showerror("Error", "Age is an integer number")
        return False

    def check_wage(self):
        wage = self.wage.get()
        if wage.isdigit():
            return True
        else:
            messagebox.showerror("Error", "Wage is an integer number")
        return False