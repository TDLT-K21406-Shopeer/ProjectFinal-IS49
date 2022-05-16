from tkinter import *
from tkinter import messagebox
from View.RolePageView import *
from Controller.AdminLoginPageController import *
from Controller.EmployeeLoginPageController import *
from Model.RolePageModel import *
from Setting.MakeCenter import *

class RolePageController():
    def __init__(self,*args,**kwargs):
      self.root = Tk()
      # center(self.root)
      self.model = RolePageModel()
      self.view = RolePageView(self.root, self.model)
      self.view.button_admin.configure(command=self.admin)
      self.view.button_employee.configure(command=self.employee)
      self.root.mainloop()

    def admin(self):
      self.toplv = Toplevel(self.root)
      self.root.withdraw()
      self.admin_work = AdminLoginPageController(self.toplv)
      self.toplv.mainloop()

    def employee(self):
      self.toplv = Toplevel(self.root)
      self.root.withdraw()
      self.employee_work = EmployeeLoginPageController(self.toplv)
      self.toplv.mainloop()
