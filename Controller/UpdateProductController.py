from tkinter import *
from tkinter import messagebox
from View.UpdateProductView import *
from Model.UpdateProductModel import *

class UpdateProductController():
    def __init__(self, root, toplv, controller):
        self.root = root
        self.toplv = toplv
        self.controller = controller
        self.window = Toplevel(self.root)
        self.model = UpdateProductModel()
        self.view = UpdateProductView(self.window,controller)
        self.view.button_update.configure(command=self.update)
        self.view.button_clear.configure(command=self.clear)
        self.view.button_exit.configure(command=self.exit)
        self.view.button_logout.configure(command=self.logout)
        self.window.mainloop()

    def update(self):
        if self.check_enter():
            data ={
                "quantity":self.view.entry_quantity.get(),
                "price_in":self.view.entry_price_in.get(),
                "price_out":self.view.entry_price_out.get()
            }
            self.model.update(data,self.view.entry_name.get())
            messagebox.showinfo("Success","Update successfully")
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

    def clear(self):
        self.view.entry_name.delete(0,"end")
        self.view.entry_trademark.delete(0,"end")
        self.view.entry_quantity.delete(0,"end")
        self.view.entry_price_in.delete(0,"end")
        self.view.entry_price_out.delete(0,"end")

    def exit(self):
        self.clear()
        self.window.destroy()
        self.root.deiconify()

    def logout(self):
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if sure == True:
            self.window.destroy()
            self.root.destroy()
            self.toplv.deiconify()