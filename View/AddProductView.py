from tkinter import *
class add_product:
    def __init__(self, root, model):
        self.top = root
        self.top.geometry("1366x768")
        self.top.resizable(0, 0)
        self.top.title("Add Product")

        self.label1 = Label(root)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./Images/AddProduct.png")
        self.label1.configure(image=self.img)
        # Label1 là cái hình Figma Trinh làm á

        self.clock = Label(root)
        self.clock.place(relx=0.84, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        # Đây là cái font thui, thích đổi sao cũng được hết á
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")
        # Cái này là add time vào trang , bỏ luôn cũng được

        self.entry8 = Entry(root)
        self.entry8.place(relx=0.527, rely=0.646, width=374, height=30)
        self.entry8.configure(font="-family {Poppins} -size 12")
        self.entry8.configure(relief="flat")
        # Nó không cần cái a=StringVar rồi get,set  Entry("textvariable") cũng được

        self.button2 = Button(root)
        self.button2.place(relx=0.526, rely=0.566)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        # Hai cái này cho nút phẳng với Label á
        self.button2.configure(activebackground="#CF1E14")  # Background lúc click
        self.button2.configure(foreground="#ffffff")  # Viền nút
        self.button2.configure(background="#CF1E14")  # Background nút
        # Mấy màu này thay lại cho giống Figma
        self.button2.configure(borderwidth="0")
        # Cái này để k có viền
        self.img_but = PhotoImage(
            file="./images/button_product.png")  # ảnh này nhớ đổi tên cho đúng nha, /images kà thuộc thư mục images á
        self.button2.configure(image=self.img_but)
        # self.button2.configure(command=self.clearr) cái command này t làm cho

root = Tk()
model =""
add_product(root,model)
root.mainloop()