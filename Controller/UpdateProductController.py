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
                "quantity":self.view.entry_quanlity.get(),
                "price_in":self.view.entry_price_in.get(),
                "price_out":self.view.entry_price_out.get()
            }
            self.model.update(data,self.view.entry_name.get())
            messagebox.showinfo("Success","Update successfully")
            self.controller.clear_treeview()
            self.controller.display_data()

    def check_enter(self):
        pass

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