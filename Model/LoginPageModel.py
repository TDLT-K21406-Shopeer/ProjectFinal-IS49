from tkinter import StringVar
import pymongo

class LoginPageModel():
    def __init__(self):
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.myclient["project"]
        self.username = StringVar()
        self.password = StringVar()
        self.result = False

class AdminLoginPageModel(LoginPageModel):
    def __init__(self):
        LoginPageModel.__init__(self)
        self.mycollection =self.mydb["Admin"]
    
    def check_account(self):
        for data in (self.mycollection.find()):
            if (data["_username"] == self.username.get()) and (data["_password"] == self.password.get()):
                self.result = True
                break
        return self.result
    
class EmployeeLoginPageModel(LoginPageModel):
    def __init__(self):
        LoginPageModel.__init__(self)
        self.mycollection = self.mydb["Employee"]
    
    def check_account(self):
        for data in (self.mycollection.find()):
            if (data["_username"] == self.username.get()) and (data["_password"] == self.password.get()):
                self.result = True
                break
        return self.result