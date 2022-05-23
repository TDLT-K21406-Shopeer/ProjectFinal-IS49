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
        self.view.entry_wage.configure(textvariable = self.model.wage)
        self.view.entry_age.configure(textvariable = self.model.age)
        self.view.entry_phone.configure(textvariable = self.model.phone)
        self.view.entry_phone_sub.configure(textvariable = self.model.phone_sub)
        self.view.entry_role.configure(textvariable = self.model.role)
        self.view.entry_username.configure(textvariable = self.model.username)
        self.view.entry_password.configure(textvariable = self.model.password)
        self.view.button_add.configure(command = self.add_employee)
        self.view.button_clear.configure(command = self.clear_entry)
        self.view.button_exit.configure(command = self.exit)
        self.view.button_logout.configure(command = self.logout)
        self.window.mainloop()

    def add_employee(self):
        if self.model.check_name():
            if self.model.check_wage():
                if self.model.check_age():
                    if self.model.check_phone():
                        if self.model.check_phone_sub():
                            if self.model.check_username():
                                if self.model.check_pw():
                                    pass

    def clear_entry(self):
        self.model.name.set("")
        self.model.wage.set("")
        self.model.age.set("")
        self.model.phone.set("")
        self.model.phone_sub.set("")
        self.model.role.set("")
        self.model.username.set("")
        self.model.password.set("")
        self.view.entry_name.config(textvariable = self.model.name)
        self.view.entry_wage.config(textvariable = self.model.wage)
        self.view.entry_age.config(textvariable = self.model.age)
        self.view.entry_phone.config(textvariable = self.model.phone)
        self.view.entry_phone_sub.config(textvariable = self.model.phone_sub)
        self.view.entry_role.config(textvariable = self.model.role)
        self.view.entry_username.config(textvariable = self.model.username)
        self.view.entry_password.config(textvariable = self.model.password)
        messagebox.showinfo("Oops!","Clear successfully")

    def exit(self):
        self.window.destroy()
        self.root.deiconify()

    def logout(self):
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if sure == True:
            self.window.destroy()
            self.root.destroy()
            self.toplv.deiconify()
