from tkinter import *
from tkinter import messagebox
from View.InvoicesManagementView import *
from Model.InvoicesManagementModel import *

class InvoicesManagementController():
    sel=[]
    def __init__(self, root, toplv):
        self.root = root
        self.toplv = toplv
        self.window = Toplevel(self.root)
        self.root.withdraw()
        self.model = InvoicesManagementModel()
        self.view = InvoicesManagementView(self.window)
        self.view.tree.bind("<<TreeviewSelect>>",self.on_the_select)
        self.display_data()
        self.view.button_search.configure(command=self.search)
        self.view.button_exit.configure(command=self.exit)
        self.view.button_logout.configure(command=self.logout)
        self.window.mainloop()
    
    def display_data(self):
        pass

    def on_the_select(self):
        pass

    def search(self):
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