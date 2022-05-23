
from random import *
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
        self.mycollection = self.mydb["Employee"]

    def check_name(self):
        name = self.name.get()
        if name.strip():
            if name.isalpha():
                return True
            else:
                messagebox.showerror("Error","Invalid name")
                return False
        else:
            messagebox.showerror("Error","Please enter a valid name")
            return False

    def check_phone(self):
        phone = self.phone.get()
        if not(phone.strip()):
            messagebox.showerror("Error","Please enter a valid phone number")
            return False
        else:
            if  phone.isdigit():
                if len(phone) ==10:
                    if phone.startwith("0"):
                        return True
                    else:
                        messagebox.showerror("Error","Invalid phone number")
                else:
                    messagebox.showerror("Error","Invalid phone number")
            else:
                messagebox.showerror("Error", "Phone numbers only include numbers")
            return False

    def check_phone_sub(self):
        phone = self.phone_sub.get()
        if not(phone.strip()):
            if  phone.isdigit():
                if len(phone) ==10:
                    if phone.startwith("0"):
                        return True
                    else:
                        messagebox.showerror("Error","Invalid phone number")
                else:
                    messagebox.showerror("Error","Invalid phone number")
            else:
                messagebox.showerror("Error", "Phone numbers only include numbers")
            return False
        else:
            return True

    def check_age(self):
        age = self.age.get()
        if not(age.strip()):
            messagebox.showerror("Error","Please enter a valid age")
            return False
        else:
            if age.isdigit():
                if int(age)>=18 and int(age)<=60:
                    return True
                else:
                    messagebox.showerror("Error","Employee of working age is 18 to 60")
            else:
                messagebox.showerror("Error", "Invalid age")
            return False

    def check_wage(self):
        wage = self.wage.get()
        if not(wage.strip()):
            messagebox.showerror("Error","Please enter a valid wage")
            return False
        else:
            if wage.isdigit():
                return True
            else:
                messagebox.showerror("Error", "Invalid wage")
            return False
    
    def check_username(self):
        username =  self.username.get()
        if not(username.strip()):
            messagebox.showerror("Error","Please enter a valid username")
            return False
        else:
            for data in (self.mycollection.find()):
                if username == data["_username"]:
                    messagebox.showerror("Error", "This username has been taken. Please try another")
                    return False
            else:
                return True

    def check_pw(self):
        if not (self.password.get()).strip():
            messagebox.showerror("Error", "Please enter a valid password")
            return False
        else:
            return True

    def set_id(self):
        if self.role.get()=="Admin":
            pass
        else:
            pass