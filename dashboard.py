from tkinter import *
from turtle import width
from employee import EmpClass
from supplier import SupplierClass
from category import CategoryClass
from product import productClass
from sales import salesClass
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox
import os
import time


class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1356x735+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")

        # title
        self.icon_title = Image.open("images\logo3.png")
        self.icon_title = self.icon_title.resize((150, 125), Image.ANTIALIAS)
        self.icon_title = ImageTk.PhotoImage(self.icon_title)
        title = Label(self.root, text="Inventory Management System", image=self.icon_title, compound=LEFT, font=(
            "times new roman", 40, 'bold'), bg="#010c48", fg="white", anchor="w", padx=20).place(x=0, y=0, relwidth=1, height=70)

        # button_logout
        button_logout = Button(self.root, text="Logout", command=self.logout, font=("times new roman", 15, "bold"),
                               bg="white", bd=2, cursor='hand2').place(x=1150, y=10, height=50, width=150)

        # clock
        self.lbl_clock = Label(self.root, text="Welcome To Inventory Management System\t\t Date : DD-MM-YYYY\t\t Time : HH:MM:SS ",
                               font=("times new roman", 15), bg="black", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        # Left Menu
        self.MenuIcon = Image.open("images\logo1.jpg")
        self.MenuIcon = self.MenuIcon.resize((200, 200), Image.ANTIALIAS)
        self.MenuIcon = ImageTk.PhotoImage(self.MenuIcon)

        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        LeftMenu.place(x=0, y=102, width=200, height=600)

        lbl_menuLogo = Label(LeftMenu, image=self.MenuIcon)
        lbl_menuLogo.pack(side=TOP, fill=X)

        lftmenu_lbl = Label(LeftMenu, text="Menu", font=("times new roman", 27, "bold"), bg="cyan", bd=2, relief=RIDGE).pack(side=TOP, fill=X)
        lftmenu_1 = Button(LeftMenu, text="Employee", command=self.employee, font=("times new roman", 20, "bold"), bg="white", bd=4, cursor='hand2').pack(side=TOP, fill=X)
        lftmenu_2 = Button(LeftMenu, text="Supplier", command=self.supplier, font=("times new roman", 20, "bold"), bg="white", bd=4, cursor='hand2').pack(side=TOP, fill=X)
        lftmenu_3 = Button(LeftMenu, text="Categories", command=self.category, font=("times new roman", 20, "bold"), bg="white", bd=4, cursor='hand2').pack(side=TOP, fill=X)
        lftmenu_4 = Button(LeftMenu, text="Product", command=self.product, font=("times new roman", 20, "bold"), bg="white", bd=4, cursor='hand2').pack(side=TOP, fill=X)
        lftmenu_4 = Button(LeftMenu, text="Sales", command=self.sales, font=("times new roman", 20, "bold"), bg="white", bd=4, cursor='hand2').pack(side=TOP, fill=X)
        lftmenu_4 = Button(LeftMenu, text="Exit", command=self.exit,font=("times new roman", 20, "bold"), bg="white", bd=4, cursor='hand2').pack(side=TOP, fill=X)

        # content
        self.lbl_1 = Label(self.root, text="Total Employee\n[0]", bd=5, relief=RIDGE, bg='blue', fg='white', font=('goudy old style', 28, 'bold'))
        self.lbl_1.place(x=300, y=175, height=150, width=300)

        self.lbl_2 = Label(self.root, text="Total Supplier\n[0]", bd=5, relief=RIDGE, bg='pink', fg='white', font=('goudy old style', 28, 'bold'))
        self.lbl_2.place(x=650, y=175, height=150, width=300)

        self.lbl_3 = Label(self.root, text="Total Categories\n[0]", bd=5, relief=RIDGE, bg='orange', fg='white', font=('goudy old style', 28, 'bold'))
        self.lbl_3.place(x=1000, y=175, height=150, width=300)

        self.lbl_4 = Label(self.root, text="Total Products\n[0]", bd=5, relief=RIDGE, bg='green', fg='white', font=('goudy old style', 28, 'bold'))
        self.lbl_4.place(x=300, y=400, height=150, width=300)

        self.lbl_5 = Label(self.root, text="Total Sales\n[0]", bd=5, relief=RIDGE, bg='brown', fg='white', font=('goudy old style', 28, 'bold'))
        self.lbl_5.place(x=650, y=400, height=150, width=300)

        # footer
        lbl_footer = Label(self.root, text=" IMS - Inventory Management System ", font=("times new roman", 13, 'bold'), bg="#010c48", fg="white").pack(side=BOTTOM, fill=X)

        self.update_content()


# ____


    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = EmpClass(self.new_win)

# ____
    def supplier(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = SupplierClass(self.new_win)

# ____
    def category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CategoryClass(self.new_win)

# ____
    def product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = productClass(self.new_win)

# ____
    def sales(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = salesClass(self.new_win)

# ___
    def update_content(self):
        con = sqlite3.connect(database=r"project.db")
        cur = con.cursor()
        try:
            cur.execute("select*from product")
            product = cur.fetchall()
            self.lbl_4.config(
                text=f'Total Products\n[{str(len(product))}]')

            cur.execute("select*from supplier")
            supplier = cur.fetchall()
            self.lbl_2.config(
                text=f'Total Supplier\n[{str(len(supplier))}]')

            cur.execute("select*from category")
            category = cur.fetchall()
            self.lbl_3.config(
                text=f'Total Category\n[{str(len(category))}]')

            cur.execute("select*from employee")
            employee = cur.fetchall()
            self.lbl_1.config(
                text=f'Total Employee\n[{str(len(employee))}]')

            bill = len(os.listdir('bill'))
            self.lbl_5.config(text=f'Total Sales\n[{str(bill)}]')

            time_ = time.strftime("%I:%M:%S")
            date_ = time.strftime("%d-%m:%Y")
            self.lbl_clock.config(text=f"Welcome To Inventory Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)}", font=(
                "times new roman", 15), bg="black", fg="white")
            self.lbl_clock.after(200, self.update_content)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

    
# ___
    def logout(self):
        self.root.destroy()
        os.system("login.py")
    
    def exit(self):
        exit()
        


if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()
