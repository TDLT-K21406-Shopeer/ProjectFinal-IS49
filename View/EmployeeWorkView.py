from tkinter import *

class employee_work:
    def __init__(self, root, model):
        self.root = Tk()

        self.root.geometry('1366x768')
        self.root.resizable(False, False)
        self.root.title('Employee Work')

        self.label1 = Label(root)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/EmployeeWork.png")
        self.label1.configure(image=self.img)

        # Inventory
        self.button2 = Button(root)
        self.button2.place(x=358, y=277)
        self.button2.configure(borderwidth="0")
        self.img_but = PhotoImage(file="./images/inventory.png")
        self.button2.configure(image=self.img_but)

        # Invoice
        self.button3 = Button(root)
        self.button3.place(x=720, y=277)
        self.button3.configure(borderwidth="0")
        self.img_butt = PhotoImage(file="./images/invoice.png")
        self.button3.configure(image=self.img_butt)

        # Log out
        self.button4 = Button(root)
        self.button4.place(x=535, y=515)
        self.button4.configure(borderwidth="0")
        self.img_butto = PhotoImage(file="./images/quit.png")
        self.button4.configure(image=self.img_butto)

        self.root.mainloop()

