from tkinter import *
from View.InventoryManagementView import *

class InventoryManagementController():
    def __init__(self, root):
        self.root = root
        self.window = Toplevel(self.root)
        self.root.withdraw()
        self.view = InventoriesManagementView(self.window)
        # self.view.button_addproduct
        self.window.mainloop()
    
    def add_product(self):
        pass

    def remove_product(self):
        pass

    def update_product(self):
        pass

    def exit(self):
        pass