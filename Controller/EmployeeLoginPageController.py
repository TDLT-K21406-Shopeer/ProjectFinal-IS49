from tkinter import *
from tkinter import messagebox
from View.EmployeeLoginPageView import *
from Model.LoginPageModel import *

class EmployeeLoginPageController():
    def __init__(self, root):
        self.model = LoginPageModel()
        self.view = EmployeeLoginPageView(root, self.model)

    def login(self):
        pass