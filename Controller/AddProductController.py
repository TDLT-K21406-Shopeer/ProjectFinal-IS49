from tkinter import *
from tkinter import messagebox
from View.AddProductView import *

class AddProductController():
    def __init__(self, root, toplv):
        self.root = root
        self.toplv = toplv
        self.window = Toplevel(self.root)
        self.view = AddProductView(self.window)
        self.view.button_add.configure(command = self.add_product)
        self.view.button_clear.configure(command = self.clear_entry)
        self.view.button_exit.configure(command = self.exit)
        self.view.button_logout.configure(command = self.logout)
        self.window.mainloop()

    def add_product(self):
        pass

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