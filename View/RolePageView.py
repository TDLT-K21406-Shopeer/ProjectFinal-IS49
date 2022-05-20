from tkinter import *

class RolePageView():
    def __init__(self,root):
        root.title("G4 Store - Choose Role")
        root.geometry("1366x768")
        root.resizable(0,0)

        self.label = Label(root)
        self.label.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./Images/RolePage.png")
        self.label.configure(image=self.img)

        self.button_admin = Button(root)
        self.button_admin.place(relx=0.665, rely=0.53, width=204, height=52)
        self.button_admin.configure(relief="flat")
        self.button_admin.configure(overrelief="flat")
        self.button_admin.configure(activebackground="#ffffff")
        self.button_admin.configure(foreground="#ffffff")
        self.button_admin.configure(background="#ffffff")
        self.button_admin.configure(borderwidth="0")
        self.img_admin = PhotoImage(file="./Images/Button_Admin.png")
        self.button_admin.configure(image=self.img_admin)

        self.button_employee = Button(root)
        self.button_employee.place(relx=0.665, rely=0.63, width=204, height=52)
        self.button_employee.configure(relief="flat")
        self.button_employee.configure(overrelief="flat")
        self.button_employee.configure(activebackground="#ffffff")
        self.button_employee.configure(foreground="#ffffff")
        self.button_employee.configure(background="#ffffff")
        self.button_employee.configure(borderwidth="0")
        self.img_employee = PhotoImage(file="./Images/Button_Employee.png")
        self.button_employee.configure(image=self.img_employee)
