from tkinter import *
from tkinter import messagebox
from Controller.InventoryManagementController import *
from Controller.InvoicesManagementController import *
from View.EmployeeWorkView import *

class EmployeeWorkController():
    def __init__(self,root):
        self.root = root
        self.window = Tk()
        self.view = EmployeeWorkView(self.window)
        self.view.button_quit.configure(command=self.logout)
        self.view.button_inventory.configure(command=self.inventory)
        self.view.button_invoice.configure(command=self.invoice)
        self.window.mainloop()

    def invoice(self):
        self.wd=InvoicesManagementController(self.window,self.root)

    def inventory(self):
        self.wd=InventoryManagementController(self.window,self.root)
    
    def logout(self):
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if sure == True:
            self.window.destroy()
            self.root.deiconify()