from tkinter import *

class EmployeeWorkView():
    def __init__(self, root):
        root.geometry('1366x768')
        root.resizable(False, False)
        root.title('Employee Work')

        self.label = Label(root)
        self.label.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(master = root,file="./images/EmployeeWork.png")
        self.label.configure(image=self.img)

        # Inventory
        self.button_inventory = Button(root)
        self.button_inventory.place(relx=0.135, rely=0.3715)
        self.button_inventory.configure(relief="flat")
        self.button_inventory.configure(overrelief="flat")
        self.button_inventory.configure(activebackground="#828293")
        self.button_inventory.configure(foreground="#828293")
        self.button_inventory.configure(background="#828293")
        self.button_inventory.configure(borderwidth="0")
        self.img_inventory = PhotoImage(master = root, file="./Images/inventory.png")
        self.button_inventory.configure(image=self.img_inventory)

        # Invoice
        self.button_invoice = Button(root)
        self.button_invoice.place(relx=0.4, rely=0.3715)
        self.button_invoice.configure(relief="flat")
        self.button_invoice.configure(overrelief="flat")
        self.button_invoice.configure(activebackground="#828293")
        self.button_invoice.configure(foreground="#828293")
        self.button_invoice.configure(background="#828293")
        self.button_invoice.configure(borderwidth="0")
        self.img_invoice = PhotoImage(master = root, file="./Images/invoice.png")
        self.button_invoice.configure(image=self.img_invoice)

        # Log out
        self.button_quit = Button(root)
        self.button_quit.place(relx=0.665, rely=0.3715)
        self.button_quit.configure(relief="flat")
        self.button_quit.configure(overrelief="flat")
        self.button_quit.configure(activebackground="#828293")
        self.button_quit.configure(foreground="#828293")
        self.button_quit.configure(background="#828293")
        self.button_quit.configure(borderwidth="0")
        self.img_quit = PhotoImage(master = root, file="./Images/quit.png")
        self.button_quit.configure(image=self.img_quit)
