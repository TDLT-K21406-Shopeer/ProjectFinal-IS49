from tkinter import *
from tkinter import messagebox
from View.UpdateEmployeeView import *
from Model.UpdateEmployeeModel import *

class UpdateEmployeeController():
    def __init__(self, root, toplv, controller):
        self.root = root
        self.toplv = toplv
        self.controller = controller
        self.window = Toplevel(self.root)
        self.model = UpdateEmployeeModel()
        self.view = UpdateEmployeeView(self.window,controller)
        self.view.button_update.configure(command=self.update)
        self.view.button_clear.configure(command=self.clear)
        self.view.button_exit.configure(command=self.exit)
        self.view.button_logout.configure(command=self.logout)
        self.window.mainloop()

    def update(self):
        if self.check_enter():
            data={
                "_age":self.view.entry_age.get(),
                "_wage":self.view.entry_wage.get(),
                "_phone":self.view.entry_phone.get(),
                "_phone_sub":self.view.entry_phone_sub.get(),
                "_password":self.view.entry_password.get()
            }
            self.model.update(data,self.model.mycollection_emp,self.view.entry_username.get())
            if self.view.entry_role.get() =="Admin":
                self.model.update(data,self.model.mycollection_adm,self.view.entry_username.get())
            messagebox.showinfo("Success","Update successfully")
            self.controller.clear_treeview()
            self.controller.display_data()

    def check_enter(self):
        name =self.view.entry_name.get()
        age = self.view.entry_age.get()
        wage = self.view.entry_wage.get()
        phone = self.view.entry_phone.get()
        phone_sub = self.view.entry_phone_sub.get()
        role = self.view.entry_role.get()
        username = self.view.entry_username.get()
        password = self.view.entry_password.get()

        if name.strip():
            for i in name:
                if (i.isalpha()==False) and i!=" ":
                    messagebox.showerror("Error","Invalid name")
                    return False
            if wage.strip():
                if wage.isdigit():
                    if age.strip():
                        if age.isdigit():
                            if int(age)>=18 and int(age)<=65:
                                if phone.strip():
                                    if phone.isnumeric():
                                        if len(phone)==10 and phone.startswith("0"):
                                            if phone_sub.isdigit() or phone_sub!="0":
                                                if role.strip() and (role=="Admin" or role =="Employee"):
                                                    if username.strip():
                                                        if password.strip():
                                                            return True
                                                        else:
                                                            messagebox.showerror("Error","Please enter a valid password")
                                                            return False
                                                    else:
                                                        messagebox.showerror("Error","Please enter a valid username")
                                                        return False
                                                else:
                                                    messagebox.showerror("Error","Enter the role Admin or  role Employee")
                                                    return False
                                            else:
                                                messagebox.showerror("Error","Phone numbers only include numbers")
                                                return False
                                        else:
                                            messagebox.showerror("Error","Invalid phone")
                                            return False
                                    else:
                                        messagebox.showerror("Error","Phone numbers only include numbers")
                                        return False
                                else:
                                    messagebox.showerror("Error","Please enter a valid phone number")
                                    return False
                            else:
                                messagebox.showerror("Error","This is not a working age. ")
                        else:
                            messagebox.showerror("Error", "Invalid age")
                            return False
                    else:
                        messagebox.showerror("Error","Please enter a valid age")
                        return False
                else:
                    messagebox.showerror("Error","Invalid wage")
            else:
                messagebox.showerror("Error","Please enter a valid wage")
                return False
        else:
            messagebox.showerror("Error","Please enter a valid name")
            return False


    def clear(self):
        self.view.entry_name.delete(0,"end")
        self.view.entry_wage.delete(0,"end")
        self.view.entry_age.delete(0,"end")
        self.view.entry_phone.delete(0,"end")
        self.view.entry_phone_sub.delete(0,"end")
        self.view.entry_role.delete(0,"end")
        self.view.entry_username.delete(0,"end")
        self.view.entry_password.delete(0,"end")

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