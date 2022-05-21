from tkinter import *

class InventoriesManagementView:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768")
        self.root.resizable(0, 0)
        self.root.title("Inventory Management")

        self.label = Label(self.root)
        self.label.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(master = self.root, file="./Images/InventoryManagement.png")
        self.label.configure(image=self.img)


        self.entry_IDproduct = Entry(self.root)
        self.entry_IDproduct.place(relx=0.65, rely=0.55, width=365, height=32)
        self.entry_IDproduct.configure(background = "#fcdefc")
        self.entry_IDproduct.configure(font="Itim 18")
        self.entry_IDproduct.configure(relief="flat")


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



