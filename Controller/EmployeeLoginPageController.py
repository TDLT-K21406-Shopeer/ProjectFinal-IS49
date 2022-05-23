from tkinter import *
from tkinter import messagebox
from View.EmployeeLoginPageView import *
from Model.LoginPageModel import *
from Controller.EmployeeWorkController import *

class EmployeeLoginPageController():
    def __init__(self, root):
        self.root = root
        self.toplv = Toplevel(root)
        self.model = EmployeeLoginPageModel()
        self.view = EmployeeLoginPageView(self.toplv)
        self.view.entry_username.configure(textvariable =self.model.username)
        self.view.entry_password.configure(textvariable =self.model.password)
        self.view.button_login.configure(command = self.login)
        self.toplv.mainloop()

    def login(self):
        if (self.model.username.get()).strip():
            if (self.model.password.get()).strip():
                if self.model.check_account():
                    self.model.username.set("")
                    self.model.password.set("")
                    self.view.entry_username.config(textvariable =self.model.username)
                    self.view.entry_password.config(textvariable =self.model.password)
                    self.toplv.withdraw()
                    self.new_root = EmployeeWorkController(self.root)
                else:
                    messagebox.showerror("Error","Username or password incorrect")
                    self.model.username.set("")
                    self.model.password.set("")
                    self.view.entry_username.config(textvariable =self.model.username)
                    self.view.entry_password.config(textvariable =self.model.password)
            else:
                messagebox.showerror("Error","Please enter a password")
        else:
            messagebox.showerror("Error","Please enter a username")
