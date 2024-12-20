from ast import Delete
import sqlite3
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import os


class salesClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg='white')
        self.root.focus_force()

        # All Variables
        self.bill_list = []
        self.var_Invoice = StringVar()

    # Title
        lbl_title = Label(self.root, text=" View Customer Bill", font=("goudy old style", 35, "bold"),
                          bg="Dark Green", fg="White", bd=3, relief=RIDGE).pack(side=TOP, fill=X, padx=10, pady=20)
        lbl_invoice = Label(self.root, text="Invoice No.", font=(
            "times new roman", 15), bg="white").place(x=50, y=100)
        txt_invoice = Entry(self.root, textvariable=self.var_Invoice, font=(
            "times new roman", 15), bg="lightyellow").place(x=160, y=100, width=180, height=28)

        btn_search = Button(self.root, text="Search", command=self.search, font=("times new roman", 15, "bold"),
                            bg="#2196f3", fg="white", cursor="hand2").place(x=360, y=100, width=120, height=28)
        btn_clear = Button(self.root, text="Clear", command=self.clear, font=("times new roman", 15, "bold"),
                           bg="lightgrey", cursor="hand2").place(x=490, y=100, width=120, height=28)

    # Bill List
        sales_Frame = Frame(self.root, bd=3, relief=RIDGE)
        sales_Frame.place(x=50, y=140, width=200, height=330)

        scrolly = Scrollbar(sales_Frame, orient=VERTICAL)
        self.Sales_List = Listbox(sales_Frame, font=(
            "goudy old style", 15), bg="white", yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.Sales_List.yview)
        self.Sales_List.pack(fill=BOTH, expand=1)
        self.Sales_List.bind("<ButtonRelease-1>", self.get_data)

    # Bill Area
        bill_Frame = Frame(self.root, bd=3, relief=RIDGE)
        bill_Frame.place(x=280, y=140, width=410, height=330)

        lbl_title2 = Label(bill_Frame, text="Customer Bill Area", font=(
            "goudy old style", 20, "bold"), bg="lightblue").pack(side=TOP, fill=X)

        scrolly2 = Scrollbar(bill_Frame, orient=VERTICAL)
        self.bill_area = Text(bill_Frame, font=(
            "goudy old style", 15), bg="lightyellow", yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT, fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH, expand=1)

    # Images
        self.BillPhoto = Image.open("images/pic.jpg")
        self.BillPhoto = self.BillPhoto.resize((380, 370), Image.ANTIALIAS)
        self.BillPhoto = ImageTk.PhotoImage(self.BillPhoto)

        lbl_image = Label(self.root, image=self.BillPhoto, bd=0)
        lbl_image.place(x=700, y=100)

        self.show()

# _____________

    def show(self):
        del self.bill_list[:]
        self.Sales_List.delete(0, END)
        for i in os.listdir('bill'):
            if i.split('.')[-1] == 'txt':
                self.Sales_List.insert(END, i)
                self.bill_list.append(i.split('.')[0])

    def get_data(self, ev):
        index_ = self.Sales_List.curselection()
        file_name = self.Sales_List.get(index_)
        self.bill_area.delete('1.0', END)
        fp = open(f'bill/{file_name}', 'r')
        for i in fp:
            self.bill_area.insert(END, i)
        fp.close()

    def search(self):
        if self.var_Invoice.get() == "":
            messagebox.showerror(
                "Error", "Invoice No. is required", parent=self.root)
        else:
            if self.var_Invoice.get() in self.bill_list:
                fp = open(f'bill/{self.var_Invoice.get()}.txt', 'r')
                self.bill_area.delete('1.0', END)
                for i in fp:
                    self.bill_area.insert(END, i)
                fp.close()
            else:
                messagebox.showerror(
                    "Error", " Invalid Invoice No.", parent=self.root)

    def clear(self):
        self.show()
        self.var_Invoice.set("")
        self.bill_area.delete('1.0', END)


if __name__ == "__main__":
    root = Tk()
    obj = salesClass(root)
    root.mainloop()
