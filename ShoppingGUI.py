from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont

shop = Tk()

def about():
    messagebox.showinfo(
        "About GenCoders", "GenCoders is The Coding Team of VCET, we specialize in doing wonders and stuff that others do not think about doing.\n"
        "Founders : Pritish Mair -- Sharvin Dedhia -- Soham Waghmare")

def exitbut():
    shop.destroy()

pquanta = []
pname = []

def addcart(numb, name):
    pquanta.append(numb)
    pname.append(name)

def viewC():
    cartv = Toplevel(shop)
    quan = "The Quantity of "
    eq = " = "
    totap = "The Total Price of "
    print(pname)
    labels1 = []
    labels2 = []
    if (len(pname) == 0):
        empty="Your Cart is Empty"
        emplab= Label(cartv,text=empty)
        emplab.pack()

    else:
        for i in range(0, len(pquanta)):
            stat1 = quan + pname[int(i)] + eq + pquanta[int(i)]
            stat2 = totap + pname[int(i)] + eq + str((int(pquanta[int(i)])*100))
            label1 = Label(cartv, text=stat1)
            label1.pack()
            label2 = Label(cartv, text=stat2)
            label2.pack()
            labels1.append(label1)
            labels2.append(label2)

def log():

    def exitbutlog():
        newL.destroy()

    newL = Toplevel(w1)
    label_1 = Label(newL, text="Username")
    label_2 = Label(newL, text="Password")
    entry_1 = Entry(newL)
    entry_2 = Entry(newL, show="*")

    label_1.grid(row=0)
    label_2.grid(row=1)
    entry_1.grid(row=0, column=1)
    entry_2.grid(row=1, column=1)

    c = Checkbutton(newL, text="Keep me logged in")
    c.grid(columnspan=2)

    submit = Button(newL, text="Submit", command=exitbutlog)
    submit.grid(columnspan=3)

def clothes():
    def exitClo():
        cloth.destroy()
    cloth = Toplevel(shop)

    #product list 1 of clothes
    fontStyle1 = tkFont.Font(family="Lucida Grande", size=10)
    pro1 = Message(cloth, text="Tshirt", font=fontStyle1)
    photo1 = PhotoImage(file="tshirt.PNG")
    l1 = Label(cloth, image=photo1, text="Total Cost = 100",
               font=fontStyle1, compound=TOP)
    l1.photo = photo1
    quantity1 = Spinbox(cloth, from_=0, to=100)
    but1 = Button(cloth, text="Add to Cart", font=fontStyle1,
                  command=lambda: addcart(quantity1.get(), "T-Shirt1"))

    pro2 = Message(cloth, text="Pant", font=fontStyle1)
    photo2 = PhotoImage(file="pant.PNG")
    l2 = Label(cloth, image=photo2, text="Total cost=100",
               font=fontStyle1, compound=TOP)
    l2.photo = photo2
    quantity2 = Spinbox(cloth, from_=0, to=100)
    but2 = Button(cloth, text="Add to cart", font=fontStyle1,
                  command=lambda: addcart(quantity2.get(), "Pant1"))

    pro3 = Message(cloth, text="Coat", font=fontStyle1)
    photo3 = PhotoImage(file="coat.PNG")
    l3 = Label(cloth, image=photo3, text="Total cost = 100",
               font=fontStyle1, compound=TOP)
    l3.photo = photo3
    quantity3 = Spinbox(cloth, from_=0, to=100)
    but3 = Button(cloth, text="Add to cart", font=fontStyle1,
                  command=lambda: addcart(quantity3.get(), "Coat1"))

    pro1.grid()
    l1.grid()
    quantity1.grid()
    but1.grid()
    pro2.grid()
    l2.grid()
    quantity2.grid()
    but2.grid()
    pro3.grid()
    l3.grid()
    quantity3.grid()
    but3.grid()

    #product list 2 of clothes
    pro4 = Message(cloth, text="Tshirt", font=fontStyle1)
    photo4 = PhotoImage(file="tshirt.PNG")
    l4 = Label(cloth, image=photo4, text="Total Cost = 100",
               font=fontStyle1, compound=TOP)
    l4.photo = photo4
    quantity4 = Spinbox(cloth, from_=0, to=100)
    but4 = Button(cloth, text="Add to Cart", font=fontStyle1,
                  command=lambda: addcart(quantity4.get(), "T-Shirt2"))

    pro5 = Message(cloth, text="Pant", font=fontStyle1)
    photo5 = PhotoImage(file="pant.PNG")
    l5 = Label(cloth, image=photo5, text="Total cost=100",
               font=fontStyle1, compound=TOP)
    l5.photo = photo5
    quantity5 = Spinbox(cloth, from_=0, to=100)
    but5 = Button(cloth, text="Add to cart", font=fontStyle1,
                  command=lambda: addcart(quantity5.get(), "Pant2"))

    pro6 = Message(cloth, text="Coat", font=fontStyle1)
    photo6 = PhotoImage(file="coat.PNG")
    l6 = Label(cloth, image=photo6, text="Total cost = 100",
               font=fontStyle1, compound=TOP)
    l6.photo = photo6
    quantity6 = Spinbox(cloth, from_=0, to=100)
    but6 = Button(cloth, text="Add to cart", font=fontStyle1,
                  command=lambda: addcart(quantity6.get(), "Coat2"))

    pro4.grid(row=0, column=1)
    l4.grid(row=1, column=1)
    quantity4.grid(row=2, column=1)
    but4.grid(row=3, column=1)

    pro5.grid(row=4, column=1)
    l5.grid(row=5, column=1)
    quantity5.grid(row=6, column=1)
    but5.grid(row=7, column=1)

    pro6.grid(row=8, column=1)
    l6.grid(row=9, column=1)
    quantity6.grid(row=10, column=1)
    but6.grid(row=11, column=1)

    #product list 3 of clothes
    pro7 = Message(cloth, text="Tshirt", font=fontStyle1)
    photo7 = PhotoImage(file="tshirt.PNG")
    l7 = Label(cloth, image=photo7, text="Total Cost = 100",
               font=fontStyle1, compound=TOP)
    l7.photo = photo7
    quantity7 = Spinbox(cloth, from_=0, to=100)
    but7 = Button(cloth, text="Add to Cart", font=fontStyle1,
                  command=lambda: addcart(quantity7.get(), "T-Shirt3"))

    pro8 = Message(cloth, text="Pant", font=fontStyle1)
    photo8 = PhotoImage(file="pant.PNG")
    l8 = Label(cloth, image=photo8, text="Total cost=100",
               font=fontStyle1, compound=TOP)
    l8.photo = photo8
    quantity8 = Spinbox(cloth, from_=0, to=100)
    but8 = Button(cloth, text="Add to cart", font=fontStyle1,
                  command=lambda: addcart(quantity8.get(), "Pant3"))

    pro9 = Message(cloth, text="Coat", font=fontStyle1)
    photo9 = PhotoImage(file="coat.PNG")
    l9 = Label(cloth, image=photo9, text="Total cost = 100",
               font=fontStyle1, compound=TOP)
    l9.photo = photo9
    quantity9 = Spinbox(cloth, from_=0, to=100)
    but9 = Button(cloth, text="Add to cart", font=fontStyle1,
                  command=lambda: addcart(quantity9.get(), "Coat3"))

    pro7.grid(row=0, column=2)
    l7.grid(row=1, column=2)
    quantity7.grid(row=2, column=2)
    but7.grid(row=3, column=2)

    pro8.grid(row=4, column=2)
    l8.grid(row=5, column=2)
    quantity8.grid(row=6, column=2)
    but8.grid(row=7, column=2)

    pro9.grid(row=8, column=2)
    l9.grid(row=9, column=2)
    quantity9.grid(row=10, column=2)
    but9.grid(row=11, column=2)

    exitbu = Button(cloth, text="BACK", padx=100, pady=15, command=exitClo)
    exitbu.grid(columnspan=3)


def shoes():
    def exitShoe():
        shoe.destroy()
    shoe = Toplevel(shop)

    #product list 1 of shoe
    fontStyle1 = tkFont.Font(family="Lucida Grande", size=10)
    pro1 = Message(shoe, text="Sports", font=fontStyle1)
    photo1 = PhotoImage(file="sport.PNG")
    l1 = Label(shoe, image=photo1, text="Total Cost = 100",
               font=fontStyle1, compound=TOP)
    l1.photo = photo1
    quantity1 = Spinbox(shoe, from_=0, to=100)
    but1 = Button(shoe, text="Add to Cart", font=fontStyle1,
                  command=lambda: addcart(quantity1.get(), "Sport1"))

    pro2 = Message(shoe, text="Casuals", font=fontStyle1)
    photo2 = PhotoImage(file="casual.PNG")
    l2 = Label(shoe, image=photo2, text="Total cost=100",
               font=fontStyle1, compound=TOP)
    l2.photo = photo2
    quantity2 = Spinbox(shoe, from_=0, to=100)
    but2 = Button(shoe, text="Add to cart", font=fontStyle1,
                  command=lambda: addcart(quantity2.get(), "Casuals1"))

    pro3 = Message(shoe, text="Sneakers", font=fontStyle1)
    photo3 = PhotoImage(file="sneaker.PNG")
    l3 = Label(shoe, image=photo3, text="Total cost = 100",
               font=fontStyle1, compound=TOP)
    l3.photo = photo3
    quantity3 = Spinbox(shoe, from_=0, to=100)
    but3 = Button(shoe, text="Add to cart", font=fontStyle1,
                  command=lambda: addcart(quantity3.get(), "Sneakers1"))

    pro1.grid()
    l1.grid()
    quantity1.grid()
    but1.grid()
    pro2.grid()
    l2.grid()
    quantity2.grid()
    but2.grid()
    pro3.grid()
    l3.grid()
    quantity3.grid()
    but3.grid()

    #product list 2 of shoe
    pro4 = Message(shoe, text="Sports", font=fontStyle1)
    photo4 = PhotoImage(file="sport.PNG")
    l4 = Label(shoe, image=photo4, text="Total Cost = 100",
               font=fontStyle1, compound=TOP)
    l4.photo = photo4
    quantity4 = Spinbox(shoe, from_=0, to=100)
    but4 = Button(shoe, text="Add to Cart", font=fontStyle1,
                  command=lambda: addcart(quantity4.get(), "Sports2"))

    pro5 = Message(shoe, text="Casuals", font=fontStyle1)
    photo5 = PhotoImage(file="casual.PNG")
    l5 = Label(shoe, image=photo5, text="Total cost=100",
               font=fontStyle1, compound=TOP)
    l5.photo = photo5
    quantity5 = Spinbox(shoe, from_=0, to=100)
    but5 = Button(shoe, text="Add to cart", font=fontStyle1,
                  command=lambda: addcart(quantity5.get(), "Casuals2"))

    pro6 = Message(shoe, text="Sneakers", font=fontStyle1)
    photo6 = PhotoImage(file="sneaker.PNG")
    l6 = Label(shoe, image=photo6, text="Total cost = 100",
               font=fontStyle1, compound=TOP)
    l6.photo = photo6
    quantity6 = Spinbox(shoe, from_=0, to=100)
    but6 = Button(shoe, text="Add to cart", font=fontStyle1,
                  command=lambda: addcart(quantity6.get(), "Sneakers2"))

    pro4.grid(row=0, column=1)
    l4.grid(row=1, column=1)
    quantity4.grid(row=2, column=1)
    but4.grid(row=3, column=1)

    pro5.grid(row=4, column=1)
    l5.grid(row=5, column=1)
    quantity5.grid(row=6, column=1)
    but5.grid(row=7, column=1)

    pro6.grid(row=8, column=1)
    l6.grid(row=9, column=1)
    quantity6.grid(row=10, column=1)
    but6.grid(row=11, column=1)

    #product list 3 of shoe
    pro7 = Message(shoe, text="Sports", font=fontStyle1)
    photo7 = PhotoImage(file="sport.PNG")
    l7 = Label(shoe, image=photo7, text="Total Cost = 100",
               font=fontStyle1, compound=TOP)
    l7.photo = photo7
    quantity7 = Spinbox(shoe, from_=0, to=100)
    but7 = Button(shoe, text="Add to Cart", font=fontStyle1,
                  command=lambda: addcart(quantity7.get(), "Sports3"))

    pro8 = Message(shoe, text="Casuals", font=fontStyle1)
    photo8 = PhotoImage(file="casual.PNG")
    l8 = Label(shoe, image=photo8, text="Total cost=100",
               font=fontStyle1, compound=TOP)
    l8.photo = photo8
    quantity8 = Spinbox(shoe, from_=0, to=100)
    but8 = Button(shoe, text="Add to cart", font=fontStyle1,
                  command=lambda: addcart(quantity8.get(), "Casuals3"))

    pro9 = Message(shoe, text="Sneakers", font=fontStyle1)
    photo9 = PhotoImage(file="sneaker.PNG")
    l9 = Label(shoe, image=photo9, text="Total cost = 100",
               font=fontStyle1, compound=TOP)
    l9.photo = photo9
    quantity9 = Spinbox(shoe, from_=0, to=100)
    but9 = Button(shoe, text="Add to cart", font=fontStyle1,
                  command=lambda: addcart(quantity9.get(), "Sneakers3"))

    pro7.grid(row=0, column=2)
    l7.grid(row=1, column=2)
    quantity7.grid(row=2, column=2)
    but7.grid(row=3, column=2)

    pro8.grid(row=4, column=2)
    l8.grid(row=5, column=2)
    quantity8.grid(row=6, column=2)
    but8.grid(row=7, column=2)

    pro9.grid(row=8, column=2)
    l9.grid(row=9, column=2)
    quantity9.grid(row=10, column=2)
    but9.grid(row=11, column=2)

    exitbut = Button(shoe, text="BACK", padx=100, pady=15, command=exitShoe)
    exitbut.grid(columnspan=3)


def television():
    def exitTel():
        tele.destroy()
    tele = Toplevel(shop)

    #product list 1 of television
    fontStyle1 = tkFont.Font(family="Lucida Grande", size=10)
    pro1 = Message(tele, text="Samsung", font=fontStyle1, width=60)
    photo1 = PhotoImage(file="tv1.PNG")
    l1 = Label(tele, image=photo1, text="Total Cost = 100",
               font=fontStyle1, compound=TOP)
    l1.photo = photo1
    quantity1 = Spinbox(tele, from_=0, to=100)
    but1 = Button(tele, text="Add to Cart", font=fontStyle1,
                  command=lambda: addcart(quantity1.get(), "Samsung1"))

    pro2 = Message(tele, text="Hitachi", font=fontStyle1, width=60)
    photo2 = PhotoImage(file="tv2.PNG")
    l2 = Label(tele, image=photo2, text="Total cost=100",
               font=fontStyle1, compound=TOP)
    l2.photo = photo2
    quantity2 = Spinbox(tele, from_=0, to=100)
    but2 = Button(tele, text="Add to cart", font=fontStyle1,
                  command=lambda: addcart(quantity2.get(), "Hitachi"))

    pro3 = Message(tele, text="Sony", font=fontStyle1, width=60)
    photo3 = PhotoImage(file="tv3.PNG")
    l3 = Label(tele, image=photo3, text="Total cost = 100",
               font=fontStyle1, compound=TOP)
    l3.photo = photo3
    quantity3 = Spinbox(tele, from_=0, to=100)
    but3 = Button(tele, text="Add to cart", font=fontStyle1,
                  command=lambda: addcart(quantity3.get(), "Sony1"))

    pro1.grid()
    l1.grid()
    quantity1.grid()
    but1.grid()
    pro2.grid()
    l2.grid()
    quantity2.grid()
    but2.grid()
    pro3.grid()
    l3.grid()
    quantity3.grid()
    but3.grid()

    #product list 2 of television
    pro4 = Message(tele, text="Samsung", font=fontStyle1, width=60)
    photo4 = PhotoImage(file="tv1.PNG")
    l4 = Label(tele, image=photo4, text="Total Cost = 100",
               font=fontStyle1, compound=TOP)
    l4.photo = photo4
    quantity4 = Spinbox(tele, from_=0, to=100)
    but4 = Button(tele, text="Add to Cart", font=fontStyle1,
                  command=lambda: addcart(quantity4.get(), "Samsung2"))

    pro5 = Message(tele, text="Hitachi", font=fontStyle1, width=60)
    photo5 = PhotoImage(file="tv2.PNG")
    l5 = Label(tele, image=photo5, text="Total cost=100",
               font=fontStyle1, compound=TOP)
    l5.photo = photo5
    quantity5 = Spinbox(tele, from_=0, to=100)
    but5 = Button(tele, text="Add to cart", font=fontStyle1,
                  command=lambda: addcart(quantity5.get(), "Hitachi2"))

    pro6 = Message(tele, text="Sony", font=fontStyle1, width=60)
    photo6 = PhotoImage(file="tv3.PNG")
    l6 = Label(tele, image=photo6, text="Total cost = 100",
               font=fontStyle1, compound=TOP)
    l6.photo = photo6
    quantity6 = Spinbox(tele, from_=0, to=100)
    but6 = Button(tele, text="Add to cart", font=fontStyle1,
                  command=lambda: addcart(quantity6.get(), "Sony2"))

    pro4.grid(row=0, column=1)
    l4.grid(row=1, column=1)
    quantity4.grid(row=2, column=1)
    but4.grid(row=3, column=1)

    pro5.grid(row=4, column=1)
    l5.grid(row=5, column=1)
    quantity5.grid(row=6, column=1)
    but5.grid(row=7, column=1)

    pro6.grid(row=8, column=1)
    l6.grid(row=9, column=1)
    quantity6.grid(row=10, column=1)
    but6.grid(row=11, column=1)

    #product list 3 of television
    pro7 = Message(tele, text="Samsung", font=fontStyle1, width=60)
    photo7 = PhotoImage(file="tv1.PNG")
    l7 = Label(tele, image=photo7, text="Total Cost = 100",
               font=fontStyle1, compound=TOP)
    l7.photo = photo7
    quantity7 = Spinbox(tele, from_=0, to=100)
    but7 = Button(tele, text="Add to Cart", font=fontStyle1,
                  command=lambda: addcart(quantity7.get(), "Samsung3"))

    pro8 = Message(tele, text="Hitachi", font=fontStyle1, width=60)
    photo8 = PhotoImage(file="tv2.PNG")
    l8 = Label(tele, image=photo8, text="Total cost=100",
               font=fontStyle1, compound=TOP)
    l8.photo = photo8
    quantity8 = Spinbox(tele, from_=0, to=100)
    but8 = Button(tele, text="Add to cart", font=fontStyle1,
                  command=lambda: addcart(quantity8.get(), "Hitachi3"))

    pro9 = Message(tele, text="Sony", font=fontStyle1, width=60)
    photo9 = PhotoImage(file="tv3.PNG")
    l9 = Label(tele, image=photo9, text="Total cost = 100",
               font=fontStyle1, compound=TOP)
    l9.photo = photo9
    quantity9 = Spinbox(tele, from_=0, to=100)
    but9 = Button(tele, text="Add to cart", font=fontStyle1,
                  command=lambda: addcart(quantity9.get(), "Sony3"))

    pro7.grid(row=0, column=2)
    l7.grid(row=1, column=2)
    quantity7.grid(row=2, column=2)
    but7.grid(row=3, column=2)

    pro8.grid(row=4, column=2)
    l8.grid(row=5, column=2)
    quantity8.grid(row=6, column=2)
    but8.grid(row=7, column=2)

    pro9.grid(row=8, column=2)
    l9.grid(row=9, column=2)
    quantity9.grid(row=10, column=2)
    but9.grid(row=11, column=2)

    exitbu = Button(tele, text="BACK", padx=100, pady=15, command=exitTel)
    exitbu.grid(columnspan=3)


def sports():
    def exitspo():
        sport.destroy()
    sport = Toplevel(shop)

    #product list 1 of sports
    fontStyle1 = tkFont.Font(family="Lucida Grande", size=10)
    pro1 = Message(sport, text="Cricket kit", font=fontStyle1, width=60)
    photo1 = PhotoImage(file="sports1.PNG")
    l1 = Label(sport, image=photo1, text="Total Cost = 100",
               font=fontStyle1, compound=TOP)
    l1.photo = photo1
    quantity1 = Spinbox(sport, from_=0, to=100)
    but1 = Button(sport, text="Add to Cart", font=fontStyle1,
                  command=lambda: addcart(quantity1.get(), "Cricket kit1"))

    pro2 = Message(sport, text="Cycle", font=fontStyle1, width=60)
    photo2 = PhotoImage(file="sports2.PNG")
    l2 = Label(sport, image=photo2, text="Total cost=100",
               font=fontStyle1, compound=TOP)
    l2.photo = photo2
    quantity2 = Spinbox(sport, from_=0, to=100)
    but2 = Button(sport, text="Add to cart", font=fontStyle1,
                  command=lambda: addcart(quantity2.get(), "Cycle1"))

    pro3 = Message(sport, text="Skates", font=fontStyle1, width=60)
    photo3 = PhotoImage(file="sports3.PNG")
    l3 = Label(sport, image=photo3, text="Total cost = 100",
               font=fontStyle1, compound=TOP)
    l3.photo = photo3
    quantity3 = Spinbox(sport, from_=0, to=100)
    but3 = Button(sport, text="Add to cart", font=fontStyle1,
                  command=lambda: addcart(quantity3.get(), "Skates1"))

    pro1.grid()
    l1.grid()
    quantity1.grid()
    but1.grid()
    pro2.grid()
    l2.grid()
    quantity2.grid()
    but2.grid()
    pro3.grid()
    l3.grid()
    quantity3.grid()
    but3.grid()

    #product list 2 of sports
    pro4 = Message(sport, text="Cricket kit", font=fontStyle1, width=60)
    photo4 = PhotoImage(file="sports1.PNG")
    l4 = Label(sport, image=photo4, text="Total Cost = 100",
               font=fontStyle1, compound=TOP)
    l4.photo = photo4
    quantity4 = Spinbox(sport, from_=0, to=100)
    but4 = Button(sport, text="Add to Cart", font=fontStyle1,
                  command=lambda: addcart(quantity4.get(), "Cricket kit2"))

    pro5 = Message(sport, text="Cycle", font=fontStyle1, width=60)
    photo5 = PhotoImage(file="sports2.PNG")
    l5 = Label(sport, image=photo5, text="Total cost=100",
               font=fontStyle1, compound=TOP)
    l5.photo = photo5
    quantity5 = Spinbox(sport, from_=0, to=100)
    but5 = Button(sport, text="Add to cart", font=fontStyle1,
                  command=lambda: addcart(quantity5.get(), "Cycle2"))

    pro6 = Message(sport, text="Skates", font=fontStyle1, width=60)
    photo6 = PhotoImage(file="sports3.PNG")
    l6 = Label(sport, image=photo6, text="Total cost = 100",
               font=fontStyle1, compound=TOP)
    l6.photo = photo6
    quantity6 = Spinbox(sport, from_=0, to=100)
    but6 = Button(sport, text="Add to cart", font=fontStyle1,
                  command=lambda: addcart(quantity6.get(), "Skates2"))

    pro4.grid(row=0, column=1)
    l4.grid(row=1, column=1)
    quantity4.grid(row=2, column=1)
    but4.grid(row=3, column=1)

    pro5.grid(row=4, column=1)
    l5.grid(row=5, column=1)
    quantity5.grid(row=6, column=1)
    but5.grid(row=7, column=1)

    pro6.grid(row=8, column=1)
    l6.grid(row=9, column=1)
    quantity6.grid(row=10, column=1)
    but6.grid(row=11, column=1)

    #product list 3 of sports
    pro7 = Message(sport, text="Cricket kit", font=fontStyle1, width=60)
    photo7 = PhotoImage(file="sports1.PNG")
    l7 = Label(sport, image=photo7, text="Total Cost = 100",
               font=fontStyle1, compound=TOP)
    l7.photo = photo7
    quantity7 = Spinbox(sport, from_=0, to=100)
    but7 = Button(sport, text="Add to Cart", font=fontStyle1,
                  command=lambda: addcart(quantity7.get(), "Cricket kit3"))

    pro8 = Message(sport, text="Cycle", font=fontStyle1, width=60)
    photo8 = PhotoImage(file="sports2.PNG")
    l8 = Label(sport, image=photo8, text="Total cost=100",
               font=fontStyle1, compound=TOP)
    l8.photo = photo8
    quantity8 = Spinbox(sport, from_=0, to=100)
    but8 = Button(sport, text="Add to cart", font=fontStyle1,
                  command=lambda: addcart(quantity8.get(), "Cycle3"))

    pro9 = Message(sport, text="Skates", font=fontStyle1, width=60)
    photo9 = PhotoImage(file="sports3.PNG")
    l9 = Label(sport, image=photo9, text="Total cost = 100",
               font=fontStyle1, compound=TOP)
    l9.photo = photo9
    quantity9 = Spinbox(sport, from_=0, to=100)
    but9 = Button(sport, text="Add to cart", font=fontStyle1,
                  command=lambda: addcart(quantity9.get(), "Skates3"))

    pro7.grid(row=0, column=2)
    l7.grid(row=1, column=2)
    quantity7.grid(row=2, column=2)
    but7.grid(row=3, column=2)

    pro8.grid(row=4, column=2)
    l8.grid(row=5, column=2)
    quantity8.grid(row=6, column=2)
    but8.grid(row=7, column=2)

    pro9.grid(row=8, column=2)
    l9.grid(row=9, column=2)
    quantity9.grid(row=10, column=2)
    but9.grid(row=11, column=2)

    exitbut = Button(sport, text="BACK", padx=100, pady=15, command=exitspo)
    exitbut.grid(columnspan=3)


def Electronics():
    def exitElec():
        electro.destroy()
    electro = Toplevel(shop)

    #product list 1 of electronics
    fontStyle1 = tkFont.Font(family="Lucida Grande", size=10)
    pro1 = Message(electro, text="Camera", font=fontStyle1, width=60)
    photo1 = PhotoImage(file="electro1.PNG")
    l1 = Label(electro, image=photo1, text="Total Cost = 100",
               font=fontStyle1, compound=TOP)
    l1.photo = photo1
    quantity1 = Spinbox(electro, from_=0, to=100)
    but1 = Button(electro, text="Add to Cart", font=fontStyle1,
                  command=lambda: addcart(quantity1.get(), "Camera1"))

    pro2 = Message(electro, text="Laptop", font=fontStyle1, width=60)
    photo2 = PhotoImage(file="electro2.PNG")
    l2 = Label(electro, image=photo2, text="Total cost=100",
               font=fontStyle1, compound=TOP)
    l2.photo = photo2
    quantity2 = Spinbox(electro, from_=0, to=100)
    but2 = Button(electro, text="Add to cart", font=fontStyle1,
                  command=lambda: addcart(quantity2.get(), "Laptop1"))

    pro3 = Message(electro, text="Television", font=fontStyle1, width=60)
    photo3 = PhotoImage(file="electro3.PNG")
    l3 = Label(electro, image=photo3, text="Total cost = 100",
               font=fontStyle1, compound=TOP)
    l3.photo = photo3
    quantity3 = Spinbox(electro, from_=0, to=100)
    but3 = Button(electro, text="Add to cart", font=fontStyle1,
                  command=lambda: addcart(quantity3.get(), "Television1"))

    pro1.grid()
    l1.grid()
    quantity1.grid()
    but1.grid()
    pro2.grid()
    l2.grid()
    quantity2.grid()
    but2.grid()
    pro3.grid()
    l3.grid()
    quantity3.grid()
    but3.grid()

    #product list 2 of electronics
    pro4 = Message(electro, text="Camera", font=fontStyle1, width=60)
    photo4 = PhotoImage(file="electro1.PNG")
    l4 = Label(electro, image=photo4, text="Total Cost = 100",
               font=fontStyle1, compound=TOP)
    l4.photo = photo4
    quantity4 = Spinbox(electro, from_=0, to=100)
    but4 = Button(electro, text="Add to Cart", font=fontStyle1,
                  command=lambda: addcart(quantity4.get(), "Camera2"))

    pro5 = Message(electro, text="Laptop", font=fontStyle1, width=60)
    photo5 = PhotoImage(file="electro2.PNG")
    l5 = Label(electro, image=photo5, text="Total cost=100",
               font=fontStyle1, compound=TOP)
    l5.photo = photo5
    quantity5 = Spinbox(electro, from_=0, to=100)
    but5 = Button(electro, text="Add to cart", font=fontStyle1,
                  command=lambda: addcart(quantity5.get(), "Laptop2"))

    pro6 = Message(electro, text="Television", font=fontStyle1, width=60)
    photo6 = PhotoImage(file="electro3.PNG")
    l6 = Label(electro, image=photo6, text="Total cost = 100",
               font=fontStyle1, compound=TOP)
    l6.photo = photo6
    quantity6 = Spinbox(electro, from_=0, to=100)
    but6 = Button(electro, text="Add to cart", font=fontStyle1,
                  command=lambda: addcart(quantity6.get(), "Television2"))

    pro4.grid(row=0, column=1)
    l4.grid(row=1, column=1)
    quantity4.grid(row=2, column=1)
    but4.grid(row=3, column=1)

    pro5.grid(row=4, column=1)
    l5.grid(row=5, column=1)
    quantity5.grid(row=6, column=1)
    but5.grid(row=7, column=1)

    pro6.grid(row=8, column=1)
    l6.grid(row=9, column=1)
    quantity6.grid(row=10, column=1)
    but6.grid(row=11, column=1)

    #product list 3 of electronics
    pro7 = Message(electro, text="Camera", font=fontStyle1, width=60)
    photo7 = PhotoImage(file="electro1.PNG")
    l7 = Label(electro, image=photo7, text="Total Cost = 100",
               font=fontStyle1, compound=TOP)
    l7.photo = photo7
    quantity7 = Spinbox(electro, from_=0, to=100)
    but7 = Button(electro, text="Add to Cart", font=fontStyle1,
                  command=lambda: addcart(quantity7.get(), "Camera3"))

    pro8 = Message(electro, text="Laptop", font=fontStyle1, width=60)
    photo8 = PhotoImage(file="electro2.PNG")
    l8 = Label(electro, image=photo8, text="Total cost=100",
               font=fontStyle1, compound=TOP)
    l8.photo = photo8
    quantity8 = Spinbox(electro, from_=0, to=100)
    but8 = Button(electro, text="Add to cart", font=fontStyle1,
                  command=lambda: addcart(quantity8.get(), "Laptop3"))

    pro9 = Message(electro, text="Television", font=fontStyle1, width=60)
    photo9 = PhotoImage(file="electro3.PNG")
    l9 = Label(electro, image=photo9, text="Total cost = 100",
               font=fontStyle1, compound=TOP)
    l9.photo = photo9
    quantity9 = Spinbox(electro, from_=0, to=100)
    but9 = Button(electro, text="Add to cart", font=fontStyle1,
                  command=lambda: addcart(quantity9.get(), "Television3"))

    pro7.grid(row=0, column=2)
    l7.grid(row=1, column=2)
    quantity7.grid(row=2, column=2)
    but7.grid(row=3, column=2)

    pro8.grid(row=4, column=2)
    l8.grid(row=5, column=2)
    quantity8.grid(row=6, column=2)
    but8.grid(row=7, column=2)

    pro9.grid(row=8, column=2)
    l9.grid(row=9, column=2)
    quantity9.grid(row=10, column=2)
    but9.grid(row=11, column=2)

    exitbut = Button(electro, text="BACK", padx=100, pady=15, command=exitElec)
    exitbut.grid(columnspan=3)


shop.geometry("1350x900")
w1 = PanedWindow(sashpad=15, width=1350)
w1.pack(fill=NONE, expand=0, side="top")
left = Entry(w1, bd=10)

fontStyle = tkFont.Font(family="Lucida Grande", size=12)
fontStyle1 = tkFont.Font(family="Lucida Grande", size=10)
fontStyle2 = tkFont.Font(family="Lucida Grande", size=15, weight="bold")

#Acessories column of Home Page
acc = PanedWindow(orient=VERTICAL, width=350, sashpad=5)
acc.place(bordermode=OUTSIDE)
acc.pack(side="left")
space = Label(w1, text="      ")

access = Label(acc, font=fontStyle, text="Our Product Categories: ")
acc.add(access)
cloth = Button(acc, font=fontStyle1, text="CLOTHES", pady=25, command=clothes)
cloth.grid(row=0)
shoes = Button(acc, font=fontStyle1, text="SHOES", pady=25, command=shoes)
shoes.grid(row=1)
tele = Button(acc, font=fontStyle1, text="TELEVISION",
              pady=25, command=television)
tele.grid(row=2)
sports = Button(acc, font=fontStyle1, text="SPORTS", pady=25, command=sports)
sports.grid(row=3)
electro = Button(acc, font=fontStyle1, text="ELECTRONICS",
                 pady=25, command=Electronics)
electro.grid(row=4)
about = Button(acc, font=fontStyle1, text="ABOUT GENCODERS",
               command=about, pady=25)
about.grid(row=5)
exitButton = Button(acc, font=fontStyle1, text="EXIT",
                    command=exitbut, pady=25)
about.grid(row=6)

acc.add(cloth)
acc.add(shoes)
acc.add(tele)
acc.add(sports)
acc.add(electro)
acc.add(about)
acc.add(exitButton)

#top pane of main page
name = Label(w1, text="                  GenCoders",
             pady=5, font=fontStyle2, width=70, anchor=W)
space = Label(w1, text="                             ")
cart = Button(w1, text="View Cart", width=20, command=viewC)
login = Button(w1, text="Login", command=log)

w1.add(name)
w1.add(space)
w1.add(cart)
w1.add(login)

#product list 1 for main Page
prodl = PanedWindow(orient=VERTICAL, width=340)
prodl.place(bordermode=OUTSIDE)
prodl.pack(fill=NONE, expand=0, side="left")

pro1 = Message(prodl, text="Product 1", font=fontStyle, width=340)
photo1 = PhotoImage(file="tv.PNG")
l1 = Label(prodl, image=photo1, text="This is a television\nTotal Cost = 100",
           font=fontStyle1, compound=TOP)
quantity1 = Spinbox(prodl, from_=0, to=100)
but1 = Button(prodl, text="Add to Cart", font=fontStyle1,
              command=lambda: addcart(quantity1.get(), "TV1"))

pro2 = Message(prodl, text="Product 2", font=fontStyle, width=340)
photo2 = PhotoImage(file="printer.PNG")
l2 = Label(prodl, image=photo2, text="This is a Printer\nTotal cost=100",
           font=fontStyle1, compound=TOP)
quantity2 = Spinbox(prodl, from_=0, to=100)
but2 = Button(prodl, text="Add to cart", font=fontStyle1,
              command=lambda: addcart(quantity2.get(), "Printer1"))

pro3 = Message(prodl, text="Product 3", font=fontStyle, width=340)
photo3 = PhotoImage(file="sofaSet.PNG")
l3 = Label(prodl, image=photo3, text="This is a Sofa\nTotal cost = 100",
           font=fontStyle1, compound=TOP)
quantity3 = Spinbox(prodl, from_=0, to=100)
but3 = Button(prodl, text="Add to cart", font=fontStyle1,
              command=lambda: addcart(quantity3.get(), "Sofa1"))

prodl.add(pro1)
prodl.add(l1)
prodl.add(quantity1)
prodl.add(but1)
prodl.add(pro2)
prodl.add(l2)
prodl.add(quantity2)
prodl.add(but2)
prodl.add(pro3)
prodl.add(l3)
prodl.add(quantity3)
prodl.add(but3)

#product list 2 for Main Page
prodl2 = PanedWindow(orient=VERTICAL, width=340)
prodl2.place(bordermode=OUTSIDE)
prodl2.pack(fill=NONE, expand=0, side="left")

pro4 = Message(prodl2, text="Product 4", font=fontStyle, width=340)
photo4 = PhotoImage(file="tv.PNG")
l4 = Label(prodl2, image=photo4, text="This is a television\nTotal Cost = 100",
           font=fontStyle1, compound=TOP)
quantity4 = Spinbox(prodl2, from_=0, to=100)
but4 = Button(prodl2, text="Add to Cart", font=fontStyle1,
              command=lambda: addcart(quantity4.get(), "TV2"))

pro5 = Message(prodl2, text="Product 5", font=fontStyle, width=340)
photo5 = PhotoImage(file="printer.PNG")
l5 = Label(prodl2, image=photo5, text="This is a Printer\nTotal cost=100",
           font=fontStyle1, compound=TOP)
quantity5 = Spinbox(prodl2, from_=0, to=100)
but5 = Button(prodl2,image=photo5, text="Add to Cart", font=fontStyle1,
              command=lambda: addcart(quantity5.get(), "Printer2"))

pro6 = Message(prodl2, text="Product 6", font=fontStyle, width=340)
photo6 = PhotoImage(file="sofaSet.PNG")
l6 = Label(prodl2, image=photo6, text="This is a Sofa\nTotal cost = 100",
           font=fontStyle1, compound=TOP)
quantity6 = Spinbox(prodl2, from_=0, to=100)
but6 = Button(prodl2, text="Add to Cart", font=fontStyle1,
              command=lambda: addcart(quantity6.get(), "Sofa2"))

prodl2.add(pro4)
prodl2.add(l4)
prodl2.add(quantity4)
prodl2.add(but4)
prodl2.add(pro5)
prodl2.add(l5)
prodl2.add(quantity5)
prodl2.add(but5)
prodl2.add(pro6)
prodl2.add(l6)
prodl2.add(quantity6)
prodl2.add(but6)

#product list 3 For main Page
prodl3 = PanedWindow(orient=VERTICAL, width=340)
prodl3.place(bordermode=OUTSIDE)
prodl3.pack(fill=NONE, expand=0, side="left")

pro7 = Message(prodl3, text="Product 7", font=fontStyle, width=340)
photo7 = PhotoImage(file="tv.PNG")
l7 = Label(prodl3, image=photo7, text="This is a television\nTotal Cost = 100",
           font=fontStyle1, compound=TOP)
quantity7 = Spinbox(prodl3, from_=0, to=100)
but7 = Button(prodl3, text="Add to cart", font=fontStyle1,
              command=lambda: addcart(quantity7.get(), "TV1"))

pro8 = Message(prodl3, text="Product 8", font=fontStyle, width=340)
photo8 = PhotoImage(file="printer.PNG")
l8 = Label(prodl3, image=photo8, text="This is a Printer\nTotal cost=100",
           font=fontStyle1, compound=TOP)
quantity8 = Spinbox(prodl3, from_=0, to=100)
but8 = Button(prodl3, text="Add to cart", font=fontStyle1,
              command=lambda: addcart(quantity8.get(), "Printer3"))

pro9 = Message(prodl3, text="Product 9", font=fontStyle, width=340)
photo9 = PhotoImage(file="sofaSet.PNG")
l9 = Label(prodl3, image=photo9, text="This is a Sofa\nTotal cost = 100",
           font=fontStyle1, compound=TOP)
quantity9 = Spinbox(prodl3, from_=0, to=100)
but9 = Button(prodl3, text="Add to cart", font=fontStyle1,
              command=lambda: addcart(quantity9.get(), "Sofa3"))

prodl3.add(pro7)
prodl3.add(l7)
prodl3.add(quantity7)
prodl3.add(but7)
prodl3.add(pro8)
prodl3.add(l8)
prodl3.add(quantity8)
prodl3.add(but8)
prodl3.add(pro9)
prodl3.add(l9)
prodl3.add(quantity9)
prodl3.add(but9)

mainloop()