from tkinter import *
from tkinter import messagebox
from View.EmployeesManagementView import *
from Controller.AddEmployeeController import *

class EmployeesManagementController():
    def __init__(self, root, toplv):
        self.root = root
        self.toplv = toplv
        self.window = Toplevel(self.root)
        self.root.withdraw()
        self.view = EmployeesManagementView(self.window)
        self.view.button_add_employee.configure(command=self.add_employee)
        self.view.button_exit.configure(command=self.exit)
        self.view.button_logout.configure(command=self.logout)
        self.window.mainloop()

    def add_employee(self):
        self.window.withdraw()
        AddEmployeeController(self.window, self.toplv)

    def remove_employee(self):
        pass

    def update_employee(self):
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
        
