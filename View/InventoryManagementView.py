from tkinter import *
from tkinter.ttk import Treeview

class InventoryManagementView:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768")
        self.root.resizable(0, 0)
        self.root.title("Inventory Management")

        self.label = Label(self.root)
        self.label.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(master = self.root, file="./Images/InventoryManagement.png")
        self.label.configure(image=self.img)

        self.columns =("id", "name", "trademark","quantity","price in","price out")
        self.tree = Treeview(root)
        self.tree.place(x=25, y=106, width=715, height=635)
        self.tree.configure(
            columns=self.columns,
            selectmode="extended"
        )

        self.tree.heading('id',text= "ID", anchor= CENTER)
        self.tree.heading('name',text= "Name", anchor= W)
        self.tree.heading('trademark',text= "Trademark", anchor= W)
        self.tree.heading('quantity',text= "Quantity", anchor= CENTER)
        self.tree.heading('price in',text= "Price in", anchor= E)
        self.tree.heading('price out',text= "Price out", anchor= E)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=55, anchor=CENTER)
        self.tree.column("#2", stretch=NO, minwidth=0, width=250)
        self.tree.column("#3", stretch=NO, minwidth=0, width=100)
        self.tree.column("#4", stretch=NO, minwidth=0, width=60, anchor=CENTER)
        self.tree.column("#5", stretch=NO, minwidth=0, width=125, anchor=E)
        self.tree.column("#6", stretch=NO, minwidth=0, width=125, anchor=E)

        self.contacts=[]

        self.entry_IDproduct = Entry(self.root)
        self.entry_IDproduct.place(relx=0.67, rely=0.54, width=365, height=32)
        self.entry_IDproduct.configure(background = "#fcdefc")
        self.entry_IDproduct.configure(font="Itim 18")
        self.entry_IDproduct.configure(relief="flat")

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

        self.button_addproduct = Button(self.root)
        self.button_addproduct.place(relx=0.6574, rely=0.646)
        self.button_addproduct.configure(relief="flat")
        self.button_addproduct.configure(overrelief="flat")
        self.button_addproduct.configure(activebackground="#ffffff")
        self.button_addproduct.configure(foreground="#ffffff")
        self.button_addproduct.configure(background="#ffffff")
        self.button_addproduct.configure(borderwidth="0")
        self.img_add = PhotoImage(master = self.root, file="./images/Button_AddProduct.png")
        self.button_addproduct.configure(image=self.img_add)

        self.button_updateproduct = Button(self.root)
        self.button_updateproduct.place(relx=0.6574, rely=0.7215)
        self.button_updateproduct.configure(relief="flat")
        self.button_updateproduct.configure(overrelief="flat")
        self.button_updateproduct.configure(activebackground="#ffffff")
        self.button_updateproduct.configure(foreground="#ffffff")
        self.button_updateproduct.configure(background="#ffffff")
        self.button_updateproduct.configure(borderwidth="0")
        self.img_update = PhotoImage(master = self.root,file="./images/Button_UpdateProduct.png")
        self.button_updateproduct.configure(image=self.img_update)

        self.button_deleteproduct = Button(self.root)
        self.button_deleteproduct.place(relx=0.6574, rely=0.8045)
        self.button_deleteproduct.configure(relief="flat")
        self.button_deleteproduct.configure(overrelief="flat")
        self.button_deleteproduct.configure(activebackground="#ffffff")
        self.button_deleteproduct.configure(foreground="#ffffff")
        self.button_deleteproduct.configure(background="#ffffff")
        self.button_deleteproduct.configure(borderwidth="0")
        self.img_del = PhotoImage(master = self.root,file="./images/Button_DeleteProduct.png")
        self.button_deleteproduct.configure(image=self.img_del)

        self.button_exit = Button(self.root)
        self.button_exit.place(relx=0.71, rely=0.88)
        self.button_exit.configure(relief="flat")
        self.button_exit.configure(overrelief="flat")
        self.button_exit.configure(activebackground="#ffffff")
        self.button_exit.configure(foreground="#ffffff")
        self.button_exit.configure(background="#ffffff")
        self.button_exit.configure(borderwidth="0")
        self.img_exit = PhotoImage(master=self.root,file="./Images/Button_Exit.png")
        self.button_exit.configure(image=self.img_exit)

        self.button_logout = Button(self.root)
        self.button_logout.place(relx=0.9277, rely=0.0156)
        self.button_logout.configure(relief="flat")
        self.button_logout.configure(overrelief="flat")
        self.button_logout.configure(activebackground="#ffffff")
        self.button_logout.configure(foreground="#ffffff")
        self.button_logout.configure(background="#ffffff")
        self.button_logout.configure(borderwidth="0")
        self.img_logout = PhotoImage(master = self.root, file="./images/Button_Logout.png")
        self.button_logout.configure(image=self.img_logout)



