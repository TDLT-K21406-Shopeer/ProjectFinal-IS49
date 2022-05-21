from tkinter import *
from View.EmployeesManagementView import *

class EmployeesManagementController():
    def __init__(self, root):
        self.root = root
        self.window = Toplevel(self.root)
        self.root.withdraw()
        self.view = EmployeesManagementView(self.window)
        self.window.mainloop()

    def add_product(self):
        pass

    def remove_product(self):
        pass

    def update_product(self):
        pass

    def exit(self):
        pass 
        
