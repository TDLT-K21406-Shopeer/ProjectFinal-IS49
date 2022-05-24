from tkinter import *
from tkinter.ttk import Treeview

class InvoicesManagementView():
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x768")
        self.root.resizable(0,0)
        self.root.title("Invoices Management")

        self.label = Label(self.root)
        self.label.place(relx=0,rely=0, width=1366, height=768)
        self.img = PhotoImage(master=self.root, file="./Images/InvoicesManagement")
        self.label.configure(image=self.img)

        self.columns =("id","name","price","date","sell")
        self.tree = Treeview(self.root)
        self.tree.place(x=25, y=108, width=715, height=635)
        self.tree.configure(
            columns=self.columns,
            selectmode="extended"
        )

        self.tree.heading("id",text = "ID", anchor=W)
        self.tree.heading("name",text = "Name", anchor=W)
        self.tree.heading("price",text = "Price", anchor=W)
        self.tree.heading("date",text = "Date", anchor=W)
        self.tree.heading("sell",text = "Sell By", anchor=W)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=1)
        self.tree.column("#2", stretch=NO, minwidth=0, width=2)
        self.tree.column("#3", stretch=NO, minwidth=0, width=3)
        self.tree.column("#4", stretch=NO, minwidth=0, width=4)
        self.tree.column("#5", stretch=NO, minwidth=0, width=5)

        self.contacts = []

        self.entry_id = Entry(self.root)
        self.entry_id.place(relx=0.67, rely=0.55, width=365, height=32)
        self.entry_id.configure(background = "#fcdefc")
        self.entry_id.configure(font="Itim 18")
        self.entry_id.configure(relief="flat")

        self.button_search = Button(self.root)
        self.button_search.place(relx=0.6164, rely=0.55,height=25, width=50)
        self.button_search.configure(relief="flat")
        self.button_search.configure(overrelief="flat")
        self.button_search.configure(activebackground="#fcdefc")
        self.button_search.configure(foreground="#fcdefc")
        self.button_search.configure(background="#fcdefc")
        self.button_search.configure(borderwidth="0")
        self.img_search = PhotoImage(master=self.root, file="./images/button_search.png")
        self.button_search.configure(image=self.img_search)
