from tkinter import *

class add_employee:
    def __init__(self, root, model):
        self.root = Tk()

        self.root.geometry('1366x768')
        self.root.resizable(False, False)
        self.root.title('Add Employee')

        self.label1 = Label(root)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/AddEmployee.png")
        self.label1.configure(image=self.img)

        # Enter Employee's name
        self.entry1 = Entry(root)
        self.entry1.place(x=330, y=350, width=252, height=34)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")
        self.entry1.configure(bg="#EECCEE")

        # Enter Employee's age
        self.entry2 = Entry(root)
        self.entry2.place(x=330, y=420, width=252, height=34)
        self.entry2.configure(font="-family {Poppins} -size 12")
        self.entry2.configure(relief="flat")
        self.entry2.configure(bg="#EECCEE")

        # Enter Employee's phone
        self.entry3 = Entry(root)
        self.entry3.place(x=330, y=490, width=252, height=34)
        self.entry3.configure(font="-family {Poppins} -size 12")
        self.entry3.configure(relief="flat")
        self.entry3.configure(bg="#EECCEE")

        # Enter Employee's wage
        self.entry4 = Entry(root)
        self.entry4.place(x=850, y=350, width=250, height=34)
        self.entry4.configure(font="-family {Poppins} -size 12")
        self.entry4.configure(relief="flat")
        self.entry4.configure(bg="#EECCEE")

        # Enter Employee's username
        self.entry5 = Entry(root)
        self.entry5.place(x=850, y=420, width=250, height=34)
        self.entry5.configure(font="-family {Poppins} -size 12")
        self.entry5.configure(relief="flat")
        self.entry5.configure(bg="#EECCEE")

        # Enter Employee's password
        self.entry6 = Entry(root)
        self.entry6.place(x=850, y=490, width=252, height=34)
        self.entry6.configure(font="-family {Poppins} -size 12")
        self.entry6.configure(relief="flat")
        self.entry6.configure(bg="#EECCEE")

        # Add
        self.button1 = Button(root)
        self.button1.place(x=420, y=600)
        self.button1.configure(borderwidth="0")
        self.button1.configure(background="#E7E7E7")
        self.button1.configure(activebackground="#E7E7E7")
        self.img_but = PhotoImage(file="./images/Button_Add.png")
        self.button1.configure(image=self.img_but)

        # Clear
        self.button2 = Button(root)
        self.button2.place(x=610, y=600)
        self.button2.configure(borderwidth="0")
        self.button2.configure(background="#E7E7E7")
        self.button2.configure(activebackground="#E7E7E7")
        self.img_butt = PhotoImage(file="./images/Button_Clear.png")
        self.button2.configure(image=self.img_butt)

        # Exit
        self.button3 = Button(root)
        self.button3.place(x=800, y=600)
        self.button3.configure(borderwidth="0")
        self.button3.configure(background="#E7E7E7")
        self.button3.configure(activebackground="#E7E7E7")
        self.img_butto = PhotoImage(file="./images/Button_Exit.png")
        self.button3.configure(image=self.img_butto)

        # Log out
        self.button4 = Button(root)
        self.button4.place(x=1263, y=12)
        self.button4.configure(borderwidth="0")
        self.button4.configure(background="white")
        self.button4.configure(activebackground="white")
        self.img_buttonn = PhotoImage(file="./images/Button_Logout.png")
        self.button4.configure(image=self.img_buttonn)

        self.root.mainloop()
