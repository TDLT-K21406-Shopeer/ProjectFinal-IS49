from tkinter import *

class AddEmployeeView:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1366x768')
        self.root.resizable(False, False)
        self.root.title('Add Employee')

        self.label = Label(root)
        self.label.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(master=root,file="./images/AddEmployee.png")
        self.label.configure(image=self.img)

        # Enter Employee's name
        self.entry_name = Entry(root)
        self.entry_name.place(x=330, y=350, width=252, height=34)
        self.entry_name.configure(font="-family {Poppins} -size 12")
        self.entry_name.configure(relief="flat")
        self.entry_name.configure(bg="#EECCEE")

        # Enter Employee's age
        self.entry_age = Entry(root)
        self.entry_age.place(x=330, y=420, width=252, height=34)
        self.entry_age.configure(font="-family {Poppins} -size 12")
        self.entry_age.configure(relief="flat")
        self.entry_age.configure(bg="#EECCEE")

        # Enter Employee's phone
        self.entry_phone = Entry(root)
        self.entry_phone.place(x=330, y=490, width=252, height=34)
        self.entry_phone.configure(font="-family {Poppins} -size 12")
        self.entry_phone.configure(relief="flat")
        self.entry_phone.configure(bg="#EECCEE")

        # Enter Employee's wage
        self.entry_wage = Entry(root)
        self.entry_wage.place(x=850, y=350, width=250, height=34)
        self.entry_wage.configure(font="-family {Poppins} -size 12")
        self.entry_wage.configure(relief="flat")
        self.entry_wage.configure(bg="#EECCEE")

        # Enter Employee's entry_username
        self.entry_username = Entry(root)
        self.entry_username.place(x=850, y=420, width=250, height=34)
        self.entry_username.configure(font="-family {Poppins} -size 12")
        self.entry_username.configure(relief="flat")
        self.entry_username.configure(bg="#EECCEE")

        # Enter Employee's password
        self.entry_pw = Entry(root)
        self.entry_pw.place(x=850, y=490, width=252, height=34)
        self.entry_pw.configure(font="-family {Poppins} -size 12")
        self.entry_pw.configure(relief="flat")
        self.entry_pw.configure(bg="#EECCEE")

        # Add
        self.button_add = Button(root)
        self.button_add.place(x=420, y=600)
        self.button_add.configure(borderwidth="0")
        self.button_add.configure(background="#E7E7E7")
        self.button_add.configure(activebackground="#E7E7E7")
        self.img_add = PhotoImage(master=root,file="./images/Button_Add.png")
        self.button_add.configure(image=self.img_add)

        # Clear
        self.button_clear = Button(root)
        self.button_clear.place(x=610, y=600)
        self.button_clear.configure(borderwidth="0")
        self.button_clear.configure(background="#E7E7E7")
        self.button_clear.configure(activebackground="#E7E7E7")
        self.img_clear = PhotoImage(master=root,file="./images/Button_Clear.png")
        self.button_clear.configure(image=self.img_clear)

        # Exit
        self.button_exit = Button(root)
        self.button_exit.place(x=800, y=600)
        self.button_exit.configure(borderwidth="0")
        self.button_exit.configure(background="#E7E7E7")
        self.button_exit.configure(activebackground="#E7E7E7")
        self.img_exit = PhotoImage(master=root,file="./images/Button_Exit.png")
        self.button_exit.configure(image=self.img_exit)

        # Log out
        self.button_logout = Button(root)
        self.button_logout.place(x=1263, y=12)
        self.button_logout.configure(borderwidth="0")
        self.button_logout.configure(background="white")
        self.button_logout.configure(activebackground="white")
        self.img_logout = PhotoImage(master=root,file="./images/Button_Logout.png")
        self.button_logout.configure(image=self.img_logout)
