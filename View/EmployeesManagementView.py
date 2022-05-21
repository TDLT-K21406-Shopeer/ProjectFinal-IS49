from tkinter import *

class EmployeesManagementView:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768")
        self.root.resizable(0, 0)
        self.root.title("Employees Management")

        self.label = Label(self.root)
        self.label.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(master = self.root, file="./Images/EmployeeManagement.png")
        self.label.configure(image=self.img)


        self.entry_id = Entry(self.root)
        self.entry_id.place(relx=0.65, rely=0.55, width=365, height=32)
        self.entry_id.configure(background = "#fcdefc")
        self.entry_id.configure(font="Itim 18")
        self.entry_id.configure(relief="flat")


        self.button_add_employee = Button(self.root)
        self.button_add_employee.place(relx=0.6574, rely=0.646)
        self.button_add_employee.configure(relief="flat")
        self.button_add_employee.configure(overrelief="flat")
        self.button_add_employee.configure(activebackground="#ffffff")
        self.button_add_employee.configure(foreground="#ffffff")
        self.button_add_employee.configure(background="#ffffff")
        self.button_add_employee.configure(borderwidth="0")
        self.img_add = PhotoImage(master = self.root, file="./Images/Button_AddEmployee.png")
        self.button_add_employee.configure(image=self.img_add)

        self.button_update_employee = Button(self.root)
        self.button_update_employee.place(relx=0.6574, rely=0.7215)
        self.button_update_employee.configure(relief="flat")
        self.button_update_employee.configure(overrelief="flat")
        self.button_update_employee.configure(activebackground="#ffffff")
        self.button_update_employee.configure(foreground="#ffffff")
        self.button_update_employee.configure(background="#ffffff")
        self.button_update_employee.configure(borderwidth="0")
        self.img_update = PhotoImage(master = self.root,file="./images/Button_UpdateEmployee.png")
        self.button_update_employee.configure(image=self.img_update)

        self.button_del_employee = Button(self.root)
        self.button_del_employee.place(relx=0.6574, rely=0.8045)
        self.button_del_employee.configure(relief="flat")
        self.button_del_employee.configure(overrelief="flat")
        self.button_del_employee.configure(activebackground="#ffffff")
        self.button_del_employee.configure(foreground="#ffffff")
        self.button_del_employee.configure(background="#ffffff")
        self.button_del_employee.configure(borderwidth="0")
        self.img_del = PhotoImage(master = self.root,file="./images/Button_DeleteEmployee.png")
        self.button_del_employee.configure(image=self.img_del)

        self.button_exit = Button(self.root)
        self.button_exit.place(relx=0.73, rely=0.87)
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




