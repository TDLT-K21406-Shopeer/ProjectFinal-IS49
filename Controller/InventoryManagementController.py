from tkinter import *
from tkinter import messagebox
from View.InventoryManagementView import *
from Controller.AddProductController import *
from Controller.UpdateProductController import *
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
        self.view.button_updateproduct.configure(command=self.update_product)
        self.view.button_deleteproduct.configure(command=self.remove_product)
        self.view.button_exit.configure(command = self.exit)
        self.view.button_logout.configure(command = self.logout)
        self.window.mainloop()

    def display_data(self):
        for data in (self.model.mycollection.find()):
            self.view.contacts.append((data["_id"],data["car_name"],data["trademark"],data["quantity"],data["price_in"],data["price_out"]))
        for contact in self.view.contacts:
            self.view.tree.insert("",END,values=contact)

    def on_the_select(self,Event):
        self.sel.clear()
        for i in self.view.tree.selection():
            if i not in self.sel:
                self.sel.append(i)

    def clear_treeview(self):
        self.view.contacts.clear()
        for i in self.view.tree.get_children():
            self.view.tree.delete(i)

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
        AddProductController(self.window, self.toplv,self)

    def remove_product(self):
        val=[]
        to_del=[]
        if len(self.sel)!=0:
            sure = messagebox.askyesno("Confirm", "Are you sure you want to delete this product?")
            if sure == True:
                for i in self.sel:
                    for j in self.view.tree.item(i)["values"]:
                        val.append(j)

                for i in range(len(val)):
                    if i%6==0:
                        to_del.append(val[i])
                for i in to_del:
                    self.model.mycollection.delete_one({"_id":i})
                messagebox.showinfo("Success!","Product was deleted successfully")
                self.sel.clear()
                self.clear_treeview()
                self.display_data()
        else:
            messagebox.showerror("Error","Please select a product!")

    def update_product(self):
        if len(self.sel)==1:
            self.val=[]
            for i in self.sel:
                for j in self.view.tree.item(i)["values"]:
                    self.val.append(j)
            self.window.withdraw()
            UpdateProductController(self.window,self.toplv,self)
        elif len(self.sel)==0:
            messagebox.showerror("Error","Please choose a product to update.")
        else:
            messagebox.showerror("Error","Can only update one product at a time.")

    def exit(self):
        self.window.destroy()
        self.root.deiconify()

    def logout(self):
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if sure == True:
            self.window.destroy()
            self.root.destroy()
            self.toplv.deiconify()