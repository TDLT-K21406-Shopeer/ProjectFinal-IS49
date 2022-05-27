from faulthandler import disable
from tkinter import *
class UpdateProductView():
    def __init__(self, root,controller):
        root.geometry("1366x768")
        root.resizable(0, 0)
        root.title("UPdate Product")

        self.label = Label(root)
        self.label.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(master=root,file="./Images/UpdateProduct.png")
        self.label.configure(image=self.img)

        self.entry_name = Entry(root)
        self.entry_name.place(x=320, y=390, width=280, height=34)
        self.entry_name.configure(font="Itim 14")
        self.entry_name.configure(relief="flat")
        self.entry_name.configure(bg="#E7CAEC")

        self.entry_trademark = Entry(root)
        self.entry_trademark.place(x=850, y=390, width=280, height=34)
        self.entry_trademark.configure(font="Itim 14")
        self.entry_trademark.configure(relief="flat")
        self.entry_trademark.configure(bg="#E7CAEC")

        self.entry_quantity = Entry(root)
        self.entry_quantity.place(x=320, y=490, width=280, height=34)
        self.entry_quantity.configure(font="Itim 14")
        self.entry_quantity.configure(relief="flat")
        self.entry_quantity.configure(bg="#E7CAEC")

        self.entry_price_in = Entry(root)
        self.entry_price_in.place(x=850, y=490, width=280, height=34)
        self.entry_price_in.configure(font="Itim 14")
        self.entry_price_in.configure(relief="flat")
        self.entry_price_in.configure(bg="#E7CAEC")

        self.entry_price_out = Entry(root)
        self.entry_price_out.place(x=320, y=590, width=280, height=34)
        self.entry_price_out.configure(font="Itim 14")
        self.entry_price_out.configure(relief="flat")
        self.entry_price_out.configure(bg="#E7CAEC")

        self.button_update = Button(root)
        self.button_update.place(x=470, y=655)
        self.button_update.configure(borderwidth="0")
        self.button_update.configure(background="#E7E7E7")
        self.button_update.configure(activebackground="#E7E7E7")
        self.img_update = PhotoImage(master=root,file="./images/Button_Update.png")
        self.button_update.configure(image=self.img_update)

        # Clear
        self.button_clear = Button(root)
        self.button_clear.place(x=640, y=655)
        self.button_clear.configure(borderwidth="0")
        self.button_clear.configure(background="#E7E7E7")
        self.button_clear.configure(activebackground="#E7E7E7")
        self.img_clear = PhotoImage(master=root,file="./images/Button_Clear.png")
        self.button_clear.configure(image=self.img_clear)

        # Exit
        self.button_exit = Button(root)
        self.button_exit.place(x=810, y=655)
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

        self.entry_name.insert(0,controller.val[1])
        self.entry_name.configure(
            state=DISABLED,
            disabledbackground="#E7CAEC",
            disabledforeground="#ffffff")
        self.entry_trademark.insert(0,controller.val[2])
        self.entry_quantity.insert(0,controller.val[3])
        self.entry_price_in.insert(0,controller.val[4])
        self.entry_price_out.insert(0,controller.val[5])
