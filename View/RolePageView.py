from tkinter import *
# from Model.RolePageModel import *

class RolePageView():
    def __init__(self,root,model):
        root.title("G4 Store - Choose Role")
        root.geometry("1366x768")
        root.resizable(0,0)
        self.model = model

        self.label = Label(root)
        self.label.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./Images/RolePage.png")
        self.label.configure(image=self.img)

        self.button_admin = Button(root)
        self.button_admin.place(relx=0.5, rely=0.5, width=204, height=52)
        self.button_admin.configure(relief="flat")
        self.button_admin.configure(overrelief="flat")
        self.button_admin.configure(activebackground="red")
        self.button_admin.configure(foreground="blue")
        self.button_admin.configure(background="grey")
        self.button_admin.configure(borderwidth="0")
        self.img_admin = PhotoImage(file="./Images/Button_Admin.png")
