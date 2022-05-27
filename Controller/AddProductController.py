from tkinter import *
from tkinter import messagebox
from Model.AddProductModel import *
from View.AddProductView import *

class AddProductController():
    def __init__(self, root, toplv, controller):
        self.controller = controller
        self.root = root
        self.toplv = toplv
        self.window = Toplevel(self.root)
        self.model = AddProductModel()
        self.view = AddProductView(self.window)
        self.view.button_add.configure(command = self.add_product)
        self.view.button_clear.configure(command = self.clear_entry)
        self.view.button_exit.configure(command = self.exit)
        self.view.button_logout.configure(command = self.logout)
        self.window.mainloop()

    def add_product(self):
        if self.check_enter():
            for data in (self.model.mycollection.find()):
                if data["car_name"] == self.view.entry_name.get() and data["trademark"] == self.view.entry_trademark.get():
                    messagebox.showerror("Error","This product was added => Update")
                    return False
            else:
                car_id = self.model.create_id()
                data = {
                    "_id": car_id,
                    "car_name":self.view.entry_name.get(),
                    "trademark":self.view.entry_trademark.get(),
                    "quantity":self.view.entry_quantity.get(),
                    "price_in":self.view.entry_price_in.get(),
                    "price_out":self.view.entry_price_out.get()
                }
                self.model.add_data(data)
            messagebox.showinfo("Success","This product was added successfully.")
            self.controller.clear_treeview()
            self.controller.display_data()

    def check_enter(self):
        name = self.view.entry_name.get()
        trademark = self.view.entry_trademark.get()
        quantity = self.view.entry_quantity.get()
        price_in = self.view.entry_price_in.get()
        price_out = self.view.entry_price_out.get()

        if name.strip():
            if trademark.strip():
                if quantity.strip():
                    if quantity.isdigit():
                        if price_in.strip():
                            if price_in.isdigit():
                                if price_out.strip():
                                    if price_out.isdigit():
                                        return True
                                    else:
                                        messagebox.showerror("Error","Invalid price out")
                                        return False
                                else:
                                    messagebox.showerror("Error","Please enter a valid price_out")
                                    return False
                            else:
                                messagebox.showerror("Error","Invalid price in")
                                return False
                        else:
                            messagebox.showerror("Error","Please enter a valid price in")
                            return False
                    else:
                        messagebox.showerror("Error","Invalid quantity")
                        return False
                else:
                    messagebox.showerror("Error","Please enter a valid quantity")
                    return False
            else:
                messagebox.showerror("Error","Please enter a valid trade mark")
                return False
        else:
            messagebox.showerror("Error","Please enter a valid name")
            return False


    def clear_entry(self):
        self.view.entry_name.delete(0,"end")
        self.view.entry_trademark.delete(0,"end")
        self.view.entry_quantity.delete(0,"end")
        self.view.entry_price_in.delete(0,"end")
        self.view.entry_price_out.delete(0,"end")

    def exit(self):
        self.window.destroy()
        self.root.deiconify()

    def logout(self):
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if sure == True:
            self.window.destroy()
            self.root.destroy()
            self.toplv.deiconify()