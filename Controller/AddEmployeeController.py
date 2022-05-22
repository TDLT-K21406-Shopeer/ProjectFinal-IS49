from tkinter import *
from tkinter import messagebox
from View.AddEmployeeView import *
from Model.AddEmployeeModel import *

class AddEmployeeController():
    def __init__(self, root, toplv):
        self.root = root
        self.toplv = toplv
        self.window = Toplevel(self.root)
        self.model = AddEmployeeModel()
        self.view = AddEmployeeView(self.window)
        self.view.entry_name.configure(textvariable = self.model.name)
        self.view.entry_age.configure(textvariable = self.model.age)
        self.view.entry_wage.configure(textvariable = self.model.wage)
        self.view.entry_phone.configure(textvariable = self.model.phone)
        self.view.entry_username.configure(textvariable = self.model.username)
        self.view.entry_password.configure(textvariable = self.model.password)
        self.view.button_add.configure(command = self.add_employee)
        self.view.button_clear.configure(command = self.clear_entry)
        self.view.button_exit.configure(command = self.exit)
        self.view.button_logout.configure(command = self.logout)
        self.window.mainloop()

    def add_employee(self):
        self.model.check_quantity()
        self.model.check_price()

    def clear_entry(self):
        pass

    def exit(self):
        self.window.destroy()
        self.root.deiconify()

    def logout(self):
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if sure == True:
            self.window.destroy()
            self.root.destroy()
            self.toplv.deiconify()
