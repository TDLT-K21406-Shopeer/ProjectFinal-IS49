from logging import root
from tkinter import *

class AdminWorkView():
    def __init__(self, root, model):
        self.model = model
        root.title("Admin's Options")
        root.geometry("1366x768")
        root.resizable(0,0)

        self.label = Label(root)
        self.label.place(relx=0, rely=0, width=1366, height=768)
        self.img_label = PhotoImage(master = root, file="./Images/AdminWork.png")
        self.label.configure(image=self.img_label)

        self.button_inventory = Button(root)
        self.button_inventory.place(relx=0.2676, rely=0.3651)
        self.button_inventory.configure(relief="flat")
        self.button_inventory.configure(overrelief="flat")
        self.button_inventory.configure(activebackground="#828293")
        self.button_inventory.configure(foreground="#828293")
        self.button_inventory.configure(background="#828293")
        self.button_inventory.configure(borderwidth="0")
        self.img_inventory = PhotoImage(master = root, file="./Images/inventory.png")
        self.button_inventory.configure(image=self.img_inventory)

        self.button_employee = Button(root)
        self.button_employee.place(relx=0.53, rely=0.3651)
        self.button_employee.configure(relief="flat")
        self.button_employee.configure(overrelief="flat")
        self.button_employee.configure(activebackground="#828293")
        self.button_employee.configure(foreground="#828293")
        self.button_employee.configure(background="#828293")
        self.button_employee.configure(borderwidth="0")
        self.img_employee = PhotoImage(master = root, file="./Images/employee.png")
        self.button_employee.configure(image=self.img_employee)

        self.button_quit = Button(root)
        self.button_quit.place(relx=0.53, rely=0.6676)
        self.button_quit.configure(relief="flat")
        self.button_quit.configure(overrelief="flat")
        self.button_quit.configure(activebackground="#828293")
        self.button_quit.configure(foreground="#828293")
        self.button_quit.configure(background="#828293")
        self.button_quit.configure(borderwidth="0")
        self.img_quit = PhotoImage(master = root, file="./Images/quit.png")
        self.button_quit.configure(image=self.img_quit)

        self.button_invoice = Button(root)
        self.button_invoice.place(relx=0.2676, rely=0.6676)
        self.button_invoice.configure(relief="flat")
        self.button_invoice.configure(overrelief="flat")
        self.button_invoice.configure(activebackground="#828293")
        self.button_invoice.configure(foreground="#828293")
        self.button_invoice.configure(background="#828293")
        self.button_invoice.configure(borderwidth="0")
        self.img_invoice = PhotoImage(master = root, file="./Images/invoice.png")
        self.button_invoice.configure(image=self.img_invoice)