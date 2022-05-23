from tkinter import *
from tkinter import messagebox
from View.EmployeesManagementView import *
from Controller.AddEmployeeController import *
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
        self.view.button_exit.configure(command=self.exit)
        self.view.button_logout.configure(command=self.logout)
        self.window.mainloop()

    def display_data(self):
        for data in (self.model.mycollection.find()):
            self.view.contacts.append((data["_id"],data["_name"],data["_role"],data["_phone"],data["_age"],data["_wage"],data["_username"]))
        for contact in self.view.contacts:
            self.view.tree.insert("",END,values=contact)

    def on_the_select(self,Event):
        self.sel.clear()
        for i in self.view.tree.selection():
            if i not in self.sel:
                self.sel.append(i)

    def clear_treeview(self):
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
        AddEmployeeController(self.window, self.toplv)

    def remove_employee(self):
        pass

    def update_employee(self):
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
        
