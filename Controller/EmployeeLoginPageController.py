from tkinter import *
from tkinter import messagebox
from View.EmployeeLoginPageView import *
from Model.LoginPageModel import *
from Controller.EmployeeWorkController import *

class EmployeeLoginPageController():
    def __init__(self, root):
        self.root = root
        self.model = EmployeeLoginPageModel()
        self.view = EmployeeLoginPageView(root)
        self.view.entry_username.configure(textvariable =self.model.username)
        self.view.entry_password.configure(textvariable =self.model.password)
        self.view.button_login.configure(command = self.login)

    def login(self):
        if self.model.check_account():
            self.model.username.set("")
            self.model.password.set("")
            self.view.entry_username.config(textvariable =self.model.username)
            self.view.entry_password.config(textvariable =self.model.password)
            self.root.withdraw()
            # self.new_root = EmployeeWorkController()


        else:
            messagebox.showerror("Error","Username or password incorrect")
            self.model.username.set("")
            self.model.password.set("")
            self.view.entry_username.config(textvariable =self.model.username)
            self.view.entry_password.config(textvariable =self.model.password)
