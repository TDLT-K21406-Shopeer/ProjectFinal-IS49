from tkinter import *

class EmployeeLoginPageView():
    def __init__(self, root, model):
        root.title("Employee Login")
        root.geometry("1366x768")
        root.resizable(0,  0)
        self.model = model

        self.label = Label(root)
        self.label.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./Images/EmployeeLogin.png")
        self.label.configure(image=self.img)

        self.button_login = Button(root)
        self.button_login.place(relx=0.7, rely=0.5, width=204, height=52)
        self.button_login.configure(relief="flat")
        self.button_login.configure(overrelief="flat")
        self.button_login.configure(activebackground="#ffffff")
        self.button_login.configure(foreground="#ffffff")
        self.button_login.configure(background="#ffffff")
        self.button_login.configure(borderwidth="0")
        self.img_login = PhotoImage(file="./Images/Button_Login.png")
        self.button_login.configure(image=self.img_login)
