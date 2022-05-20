from tkinter import *

class EmployeeLoginPageView():
    def __init__(self, root):
        root.title("Employee Login")
        root.geometry("1366x768")
        root.resizable(0,  0)

        self.label = Label(root)
        self.label.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./Images/EmployeeLogin.png")
        self.label.configure(image=self.img)

        self.button_login = Button(root)
        self.button_login.place(relx=0.6625, rely=0.725, width=204, height=52)
        self.button_login.configure(relief="flat")
        self.button_login.configure(overrelief="flat")
        self.button_login.configure(activebackground="#ffffff")
        self.button_login.configure(foreground="#ffffff")
        self.button_login.configure(background="#ffffff")
        self.button_login.configure(borderwidth="0")
        self.img_login = PhotoImage(file="./Images/Button_Login.png")
        self.button_login.configure(image=self.img_login)
        
        self.entry_username = Entry(root)
        self.entry_username.place(relx=0.62, rely=0.521, width=350, height=30)
        self.entry_username.configure(font="Itim 18")
        self.entry_username.configure(relief="flat")
        self.entry_username.configure(bg="grey")

        self.entry_password = Entry(root)
        self.entry_password.place(relx=0.62, rely=0.645, width=350, height=30)
        self.entry_password.configure(font="Itim 18")
        self.entry_password.configure(relief="flat")
        self.entry_password.configure(show="*")
        self.entry_password.configure(bg="grey")
