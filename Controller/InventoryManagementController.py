from tkinter import *
from tkinter import messagebox
from View.InventoryManagementView import *
from Controller.AddProductController import *
from Model.InventoryManagementModel import *

class InventoryManagementController():
    sel=[]
    def __init__(self, root, toplv):
        self.root = root
        self.toplv = toplv
        self.window = Toplevel(self.root)
        self.root.withdraw()
        self.model = InventoryManagementModel()
        self.view = InventoryManagementView(self.window)
        self.view.tree.bind("<<TreeviewSelect>>",self.on_the_select)
        self.display_data()
        self.view.button_search.configure(command=self.search_product)
        self.view.button_addproduct.configure(command=self.add_product)
        self.view.button_exit.configure(command = self.exit)
        self.view.button_logout.configure(command = self.logout)
        self.window.mainloop()

    def display_data(self):
        for data in (self.model.mycollection.find()):
            self.view.contacts.append((data["_id"],data["car_name"],data["quantity"],data["price_in"],data["price_out"]))
        for contact in self.view.contacts:
            self.view.tree.insert("",END,values=contact)

    def on_the_select(self,Event):
        self.sel.clear()
        for i in self.view.tree.selection():
            if i not in self.sel:
                self.sel.append(i)

    def search_product(self):
        val=[]
        for i in self.view.tree.get_children():
            val.append(i)
            for j in self.view.tree.item(i)["values"]:
                val.append(j)

        to_search = self.view.entry_IDproduct.get()
        for search in val:
            if search == to_search:
                self.view.tree.selection_set(val[val.index(search)-1])
                self.view.tree.focus(val[val.index(search)-1])
                messagebox.showinfo("Success!","Product ID: {} found.".format(self.view.entry_IDproduct.get()))

                break
        else:
            messagebox.showerror("Error","Not found product")

    
    def add_product(self):
        self.window.withdraw()
        AddProductController(self.window, self.toplv)

    def remove_product(self):
        pass

    def update_product(self):
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