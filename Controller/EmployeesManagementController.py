from tkinter import *
from tkinter import messagebox
from View.EmployeesManagementView import *
from Controller.AddEmployeeController import *
from Controller.UpdateEmployeeController import *
from Model.EmployeesManagementModel import *

class EmployeesManagementController():
    sel=[]
    def __init__(self, root, toplv):
        self.root = root
        self.toplv = toplv
        self.window = Toplevel(self.root)
        self.root.withdraw()
        self.model = EmployeesManagementModel()
        self.view = EmployeesManagementView(self.window)
        self.view.tree.bind("<<TreeviewSelect>>", self.on_the_select)
        self.display_data()
        self.view.button_search.configure(command=self.search_emp)
        self.view.button_add_employee.configure(command=self.add_employee)
        self.view.button_update_employee.configure(command=self.update_employee)
        self.view.button_del_employee.configure(command=self.remove_employee)
        self.view.button_exit.configure(command=self.exit)
        self.view.button_logout.configure(command=self.logout)
        self.window.mainloop()

    def display_data(self):
        for data in (self.model.mycollection_emp.find()):
            self.view.contacts.append((data["_id"],data["_name"],data["_role"],data["_phone"],data["_phone_sub"],data["_age"],data["_wage"],data["_username"]))
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

    def search_emp(self):
        val=[]
        for i in self.view.tree.get_children():
            val.append(i)
            for j in self.view.tree.item(i)["values"]:
                val.append(j)

        to_search = self.view.entry_id.get()
        for search in val:
            if search == to_search:
                self.view.tree.selection_set(val[val.index(search)-1])
                self.view.tree.focus(val[val.index(search)-1])
                messagebox.showinfo("Success!","Employee ID: {}".format(self.view.entry_id.get()))
                break
        else:
            messagebox.showerror("Error","Not found employee")

    def add_employee(self):
        self.window.withdraw()
        AddEmployeeController(self.window, self.toplv,self)

    def remove_employee(self):
        val=[]
        to_del=[]

        if len(self.sel)!=0:
            sure = messagebox.askyesno("Confirm", "Are you sure you want to delete this employee?")
            if sure == True:
                for i in self.sel:
                    for j in self.view.tree.item(i)["values"]:
                        val.append(j)

                for i in range(len(val)):
                    if i%8==0:
                        to_del.append(val[i])
                    
                flag = 1

                for i in to_del:
                    if i =="c000":
                        flag = 0
                        break
                    else:
                        self.model.mycollection_emp.delete_one({"_id":i})
                        if i[0]=="c":
                            self.model.mycollection_adm.delete_one({"_id":i})
                
                if flag == 1:
                    messagebox.showinfo("Success!","Employee was deleted successfully")
                    self.sel.clear()
                    self.clear_treeview()
                    self.display_data()
                else:
                    messagebox.showerror("Error","Can not delete master admin")
        else:
            messagebox.showerror("Error","Please select an employee!")

    def update_employee(self):
        if len(self.sel)==1:
            self.val=[]
            for i in self.sel:
                for j in self.view.tree.item(i)["values"]:
                    self.val.append(j)
            for data in (self.model.mycollection_emp.find()):
                if data["_id"] == self.val[0]:
                    self.pw=data["_password"]
                    break
            self.window.withdraw()
            UpdateEmployeeController(self.window,self.toplv,self)
        elif len(self.sel)==0:
            messagebox.showerror("Error","Please choose a employee to update.")
        else:
            messagebox.showerror("Error","Can only update one employee at a time.")


    def exit(self):
        self.window.destroy()
        self.root.deiconify()

    def logout(self):
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if sure == True:
            self.window.destroy()
            self.root.destroy()
            self.toplv.deiconify()
        
