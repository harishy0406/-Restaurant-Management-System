from tkinter import *
import random
import time
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from PIL import Image, ImageTk

def system():
    root = Tk()
    root.geometry("1700x800")
    root.title("Restaurant Management System By Harish")

    # Load the background image
    bg_image = Image.open("C:\\Users\\hariv\\Pictures\\PROJECTS\\HarishPortfolio\\har\\Background_img_Home.jpg")
    bg_image = bg_image.resize((1700, 800), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Create a label to display the background image
    bg_label = Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    def Database():
        global connectn, cursor
        connectn = sqlite3.connect("Restaurant.db")
        cursor = connectn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS Restaurantrecords(ordno text,piz text,bur text,ice text, dr text, ct text,sb text,tax text,sr text,tot text)")

    orderno = StringVar()
    pizza = StringVar()
    burger = StringVar()
    icecream = StringVar()
    drinks = StringVar()
    cost = StringVar()
    subtotal = StringVar()
    tax = StringVar()
    service = StringVar()
    total = StringVar()

    def tottal():
        order = (orderno.get())
        pi = float(pizza.get())
        bu = float(burger.get())
        ice = float(icecream.get())
        dr = float(drinks.get())

        costpi = pi * 80
        costbu = bu * 60
        costice = ice * 40
        costdr = dr * 40

        costofmeal = (costpi + costbu + costice + costdr)
        ptax = ((costpi + costbu + costice + costdr) * 0.18)
        sub = (costpi + costbu + costice + costdr)
        ser = ((costpi + costbu + costice + costdr) / 99)
        paidtax = str(ptax)
        Service = str(ser)
        overall = str(ptax + ser + sub)

        cost.set(costofmeal)
        tax.set(ptax)
        subtotal.set(sub)
        service.set(ser)
        total.set(overall)

    def reset():
        orderno.set("")
        pizza.set("")
        burger.set("")
        icecream.set("")
        drinks.set("")
        cost.set("")
        subtotal.set("")
        tax.set("")
        service.set("")
        total.set("")

    def exit():
        root.destroy()

    topframe = Frame(root, bg="white", width=1600, height=50)
    topframe.pack(side=TOP)

    leftframe = Frame(root, width=500, height=700)
    leftframe.pack(side=LEFT)

    rightframe = Frame(root, width=500, height=700)
    rightframe.pack(side=RIGHT)

    def DisplayData():
        Database()
        my_tree.delete(*my_tree.get_children())
        cursor = connectn.execute("SELECT * FROM Restaurantrecords")
        fetch = cursor.fetchall()
        for data in fetch:
            my_tree.insert('', 'end', values=(data))
        cursor.close()
        connectn.close()

    style = ttk.Style()
    style.configure("Treeview",
                    foreground="black",
                    rowheight=40,
                    fieldbackground="white"
                    )
    style.map('Treeview',
              background=[('selected', 'lightblue')])

    my_tree = ttk.Treeview(rightframe)
    my_tree['columns'] = ("ordno", "piz", "bur", "ice", "dr", "ct", "sb", "tax", "sr", "tot")

    horizontal_bar = ttk.Scrollbar(rightframe, orient="horizontal")
    horizontal_bar.configure(command=my_tree.xview)
    my_tree.configure(xscrollcommand=horizontal_bar.set)
    horizontal_bar.pack(fill=X, side=BOTTOM)

    vertical_bar = ttk.Scrollbar(rightframe, orient="vertical")
    vertical_bar.configure(command=my_tree.yview)
    my_tree.configure(yscrollcommand=vertical_bar.set)
    vertical_bar.pack(fill=Y, side=RIGHT)

    my_tree.column("#0", width=0, minwidth=0)
    my_tree.column("ordno", anchor=CENTER, width=80, minwidth=25)
    my_tree.column("piz", anchor=CENTER, width=60, minwidth=25)
    my_tree.column("bur", anchor=CENTER, width=50, minwidth=25)
    my_tree.column("ice", anchor=CENTER, width=80, minwidth=25)
    my_tree.column("dr", anchor=CENTER, width=50, minwidth=25)
    my_tree.column("ct", anchor=CENTER, width=50, minwidth=25)
    my_tree.column("sb", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("tax", anchor=CENTER, width=50, minwidth=25)
    my_tree.column("sr", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("tot", anchor=CENTER, width=50, minwidth=25)

    my_tree.heading("ordno", text="Order No", anchor=CENTER)
    my_tree.heading("piz", text="Pizza", anchor=CENTER)
    my_tree.heading("bur", text="Burger", anchor=CENTER)
    my_tree.heading("ice", text="Ice cream", anchor=CENTER)
    my_tree.heading("dr", text="Drinks", anchor=CENTER)
    my_tree.heading("ct", text="Cost", anchor=CENTER)
    my_tree.heading("sb", text="Subtotal", anchor=CENTER)
    my_tree.heading("tax", text="Tax", anchor=CENTER)
    my_tree.heading("sr", text="Service", anchor=CENTER)
    my_tree.heading("tot", text="Total", anchor=CENTER)

    my_tree.pack()
    DisplayData()

    def add():
        Database()
        orders = orderno.get()
        pizzas = pizza.get()
        burgers = burger.get()
        ices = icecream.get()
        drinkss = drinks.get()
        costs = cost.get()
        subtotals = subtotal.get()
        taxs = tax.get()
        services = service.get()
        totals = total.get()
        if orders == "" or pizzas == "" or burgers == "" or ices == "" or drinkss == "" or costs == "" or subtotals == "" or taxs == "" or services == "" or totals == "":
            messagebox.showinfo("Warning", "Please fill the empty field!!!")
        else:
            connectn.execute(
                'INSERT INTO Restaurantrecords (ordno, piz, bur , ice ,dr ,ct ,sb ,tax, sr, tot) VALUES (?,?,?,?,?,?,?,?,?,?)',
                (orders, pizzas, burgers, ices, drinkss, costs, subtotals, taxs, services, totals));
            connectn.commit()
            messagebox.showinfo("Message", "Stored successfully")
        DisplayData()
        connectn.close()

    def DisplayData():
        Database()
        my_tree.delete(*my_tree.get_children())
        cursor = connectn.execute("SELECT * FROM Restaurantrecords")
        fetch = cursor.fetchall()
        for data in fetch:
            my_tree.insert('', 'end', values=(data))
        cursor.close()
        connectn.close()

    def Delete():
        Database()
        if not my_tree.selection():
            messagebox.showwarning("Warning", "Select data to delete")
        else:
            result = messagebox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                            icon="warning")
        if result == 'yes':
            curItem = my_tree.focus()
            contents = (my_tree.item(curItem))
            selecteditem = contents['values']
            my_tree.delete(curItem)
            cursor = connectn.execute("DELETE FROM Restaurantrecords WHERE ordno= %d" % selecteditem[0])
            connectn.commit()
            cursor.close()
            connectn.close()

    localtime = time.asctime(time.localtime(time.time()))
    main_lbl = Label(topframe, font=('Calibri', 25, 'bold'), text="Restaurant Management System By Harish", fg="Black", anchor=W, bg="white")
    main_lbl.grid(row=0, column=0)
    main_lbl = Label(topframe, font=('Calibri', 15,), text=localtime, fg="green", anchor=W, bg="white")
    main_lbl.grid(row=1, column=0)

    ordlbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Order No.", fg="black", bd=5, anchor=W, bg="white").grid(row=1, column=0)
    ordtxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',textvariable=orderno).grid(row=1, column=1)

    pizlbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Pizza", fg="black", bd=5, anchor=W, bg="white").grid(row=2, column=0)
    piztxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',textvariable=pizza).grid(row=2, column=1)

    burlbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Burger", fg="black", bd=5, anchor=W, bg="white").grid(row=3, column=0)
    burtxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',textvariable=burger).grid(row=3, column=1)

    icelbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Ice Cream", fg="black", bd=5, anchor=W, bg="white").grid(row=4, column=0)
    icetxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',textvariable=icecream).grid(row=4, column=1)

    drinklbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Drinks", fg="black", bd=5, anchor=W, bg="white").grid(row=5, column=0)
    drinktxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',textvariable=drinks).grid(row=5, column=1)

    costlbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Cost", fg="black", bd=5, anchor=W, bg="white").grid(row=6, column=0)
    costtxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',textvariable=cost).grid(row=6, column=1)

    sublbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Subtotal", fg="black", bd=5, anchor=W, bg="white").grid(row=7, column=0)
    subtxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',textvariable=subtotal).grid(row=7, column=1)

    taxlbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Tax", fg="black", bd=5, anchor=W, bg="white").grid(row=8, column=0)
    taxtxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',textvariable=tax).grid(row=8, column=1)

    serlbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Service", fg="black", bd=5, anchor=W, bg="white").grid(row=9, column=0)
    sertxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',textvariable=service).grid(row=9, column=1)

    totlbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Total", fg="black", bd=5, anchor=W, bg="white").grid(row=10, column=0)
    tottxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',textvariable=total).grid(row=10, column=1)

    totalbtn = Button(leftframe, padx=10, pady=5, bd=10, fg="black", font=('Calibri', 16, 'bold'), width=10,text="Total", bg="white", command=tottal).grid(row=11, column=1)

    resetbtn = Button(leftframe, padx=10, pady=5, bd=10, fg="black", font=('Calibri', 16, 'bold'), width=10,text="Reset", bg="white", command=reset).grid(row=11, column=2)

    exitbtn = Button(leftframe, padx=10, pady=5, bd=10, fg="black", font=('Calibri', 16, 'bold'), width=10, text="Exit", bg="white", command=exit).grid(row=11, column=3)

    addbtn = Button(leftframe, padx=10, pady=5, bd=10, fg="black", font=('Calibri', 16, 'bold'), width=10,text="Add", bg="white", command=add).grid(row=11, column=4)

    delbtn = Button(leftframe, padx=10, pady=5, bd=10, fg="black", font=('Calibri', 16, 'bold'), width=10,text="Delete", bg="white", command=Delete).grid(row=11, column=5)

    root.mainloop()

system()
