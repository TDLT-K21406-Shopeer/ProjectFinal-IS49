from tkinter import *

class employee_management:
    def __init__(self, root, model):
        self.root = Tk()

        self.root.geometry('1366x768')
        self.root.resizable(False, False)
        self.root.title('Employee Management')

        self.label1 = Label(root)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/EmployeeManagement.png")
        self.label1.configure(image=self.img)

        # Search ID Employee
            # Button này là nguyên cái thanh Search
        self.button = Button(root)
        self.button.place(x=832, y=413)
        self.button.configure(borderwidth="0")
        self.button.configure(background="white")
        self.button.configure(activebackground="white")
        self.img_bu = PhotoImage(file="./images/Button_Search Bar.png")
        self.button.configure(image=self.img_bu)

            # Entry đè lên Button
        self.entry1 = Entry(root)
        self.entry1.place(x=900, y=415, width=395, height=32)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")
        self.entry1.configure(bg="#FFE0FF")

        # Add Employee
        self.button1 = Button(root)
        self.button1.place(x=905, y=490)
        self.button1.configure(borderwidth="0")
        self.button1.configure(background="white")
        self.button1.configure(activebackground="white")
        self.img_but = PhotoImage(file="./images/Button_AddEmployee.png")
        self.button1.configure(image=self.img_but)

        # Update Employee
        self.button2 = Button(root)
        self.button2.place(x=905, y=550)
        self.button2.configure(borderwidth="0")
        self.button2.configure(background="white")
        self.button2.configure(activebackground="white")
        self.img_butt = PhotoImage(file="./images/Button_UpdateEmployee.png")
        self.button2.configure(image=self.img_butt)

        # Delete Employee
        self.button3 = Button(root)
        self.button3.place(x=905, y=610)
        self.button3.configure(borderwidth="0")
        self.button3.configure(background="white")
        self.button3.configure(activebackground="white")
        self.img_butto = PhotoImage(file="./images/Button_DeleteEmployee.png")
        self.button3.configure(image=self.img_butto)

        # Exit
        self.button4 = Button(root)
        self.button4.place(x=980, y=672)
        self.button4.configure(borderwidth="0")
        self.button4.configure(background="white")
        self.button4.configure(activebackground="white")
        self.img_button = PhotoImage(file="./images/Button_Exit.png")
        self.button4.configure(image=self.img_button)

        # Log out
        self.button5 = Button(root)
        self.button5.place(x=1263, y=12)
        self.button5.configure(borderwidth="0")
        self.button5.configure(background="white")
        self.button5.configure(activebackground="white")
        self.img_buttonn = PhotoImage(file="./images/Button_Logout.png")
        self.button5.configure(image=self.img_buttonn)

        self.root.mainloop()
