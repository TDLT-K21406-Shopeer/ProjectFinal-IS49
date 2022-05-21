from tkinter import *
class InventoriesManagementView:
    def __init__(self, root, model):
        self.top.geometry("1366x768")
        self.top.resizable(0, 0)
        self.top.title("Inventory Management")

        self.label1 = Label(root)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(
            file="./images/InventoryManagement.png")
        self.label1.configure(image=self.img)


        self.entry_IDproduct = Entry(root)
        self.entry_IDproduct.place(relx=0.3, rely=0.4, width=374, height=30)
        self.entry_IDproduct.configure(font="-family {Poppins} -size 12")
        self.entry_IDproduct.configure(relief="flat")


        self.button_addproduct = Button(root)
        self.button_addproduct.place(relx=0.5, rely=0.3, width=204, height=52)
        self.button_addproduct.configure(relief="flat")
        self.button_addproduct.configure(overrelief="flat")
        self.button_addproduct.configure(activebackground="#CF1E14")
        self.button_addproduct.configure(foreground="#ffffff")
        self.button_addproduct.configure(background="#CF1E14")
        self.button_addproduct.configure(borderwidth="0")
        self.img_but = PhotoImage(
            file="./images/Button_AddProduct.png")
        self.button_addproduct.configure(image=self.img_but)

        self.button_updateproduct = Button(root)
        self.button_updateproduct.place(relx=0.55, rely=0.35, width=204, height=52)
        self.button_updateproduct.configure(relief="flat")
        self.button_updateproduct.configure(overrelief="flat")
        self.button_updateproduct.configure(activebackground="#CF1E14")
        self.button_updateproduct.configure(foreground="#ffffff")
        self.button_updateproduct.configure(background="#CF1E14")
        self.button_updateproduct.configure(borderwidth="0")
        self.img_but = PhotoImage(
            file="./images/Button_UpdateProduct.png")
        self.button_updateproduct.configure(image=self.img_but)

        self.button_deleteproduct = Button(root)
        self.button_deleteproduct.place(relx=0.6, rely=0.4, width=204, height=52)
        self.button_deleteproduct.configure(relief="flat")
        self.button_deleteproduct.configure(overrelief="flat")
        self.button_deleteproduct.configure(activebackground="#CF1E14")
        self.button_deleteproduct.configure(foreground="#ffffff")
        self.button_deleteproduct.configure(background="#CF1E14")
        self.button_deleteproduct.configure(borderwidth="0")
        self.img_but = PhotoImage(
            file="./images/Button_DeleteProduct.png")
        self.button_deleteproduct.configure(image=self.img_but)

        self.button_exit = Button(root)
        self.button_exit.place(relx=0.7, rely=0.7, width=204, height=52)
        self.button_exit.configure(relief="flat")
        self.button_exit.configure(overrelief="flat")
        self.button_exit.configure(activebackground="#ffffff")
        self.button_exit.configure(foreground="#ffffff")
        self.button_exit.configure(background="#ffffff")
        self.button_exit.configure(borderwidth="0")
        self.img_exit = PhotoImage(file="./Images/Button_Admin.png")
        self.button_exit.configure(image=self.img_exit)



