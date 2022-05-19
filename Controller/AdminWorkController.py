from tkinter import *
from tkinter import messagebox
from View.AdminWorkView import *
from Model.AdminWorkModel import *


class AdminWorkController():
    def __init__(self):
        self.root = Tk()
        self.model = AdminWorkModel()
        self.view = AdminWorkView(self.root, self.model)
        self.root.mainloop()