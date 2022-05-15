from tkinter import *
from View.RolePageView import *
from Model.RolePageModel import *
from Setting.MakeCenter import *

class RolePageController():
    def __init__(self,*args,**kwargs):
      self.root = Tk()
      center(self.root)
      self.model = RolePageModel()
      self.view = RolePageView(self.root, self.model)
      self.root.mainloop()