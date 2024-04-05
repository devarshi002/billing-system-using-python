from tkinter import *
import win32api
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders














def clear_fields():
    name_entry.delete(0, END)
    phone_entry.delete(0, END)
    bill_number_entry.delete(0, END)
    VegpizzaEntry.delete(0, END)
    PaneerpizzaEntry.delete(0, END)
    cheezpizzaEntry.delete(0, END)
    ItalianpizzaEntry.delete(0, END)
    GreekpizzaEntry.delete(0, END)
    MargeritapizzaEntry.delete(0, END)
    SteamVegmomosEntry.delete(0, END)
    FriedVegmomosEntry.delete(0, END)
    SteampaneermomosEntry.delete(0, END)
    FriedpaneermomosEntry.delete(0, END)
    ChickenmomosEntry.delete(0, END)
    ChillimomosEntry.delete(0, END)
    BurgerEntry.delete(0, END)
    SandwichEntry.delete(0, END)
    CachoriEntry.delete(0, END)
    ColdcofeeEntry.delete(0, END)
    ManchurianEntry.delete(0, END)
    NoodlesEntry.delete(0, END)


root = Tk()
root.title('Cafe Bill system')
root.geometry('1920x1080')
root.iconbitmap('logo.ico')

# Heading label
heading_label = Label(root, text="Cafe Billing System", font=("times new roman", 30, "bold"), bg="hot pink", fg="black", bd=7)
heading_label.pack(fill=X)

# Customer details frame
customer_details_frame = LabelFrame(root, text="Customer Details", font=("times new roman", 15, "bold"), bg="pink", fg="black", bd=5)
customer_details_frame.pack(fill=X, padx=10)

# Name label and entry field
name_label = Label(customer_details_frame, text="Name", font=("times new roman", 20, "bold"), bg="pink", fg="black", bd=2, width=8)
name_label.grid(row=0, column=0, padx=20,)
name_entry = Entry(customer_details_frame, font=('arial', 15), bd=3)
name_entry.grid(row=0, column=1, padx=18)

# Phone label and entry field
phone_label = Label(customer_details_frame, text="Phone Number", font=("times new roman", 20, "bold"), bg="pink", fg="black", bd=2, width=11)
phone_label.grid(row=0, column=2, padx=20, pady=2)
phone_entry = Entry(customer_details_frame, font=('arial', 15), bd=3)
phone_entry.grid(row=0, column=3, padx=18)

# Bill Number label and entry field
bill_number_label = Label(customer_details_frame, text="Bill Number", font=("times new roman", 20, "bold"), bg="pink", fg="black", bd=2, width=10)
bill_number_label.grid(row=0, column=4, padx=20, pady=2)
bill_number_entry = Entry(customer_details_frame, font=('arial', 15), bd=3)
bill_number_entry.grid(row=0, column=5, padx=18)


searchButton=Button(customer_details_frame, text="Search", font=('arial', 12, "bold"), bd=3)
searchButton.grid(row=0,column=6,padx=20, pady=8)



# menu section

productsFrame = Frame(root)
productsFrame.pack(pady=10)

# pizza div
PizzaFrame = LabelFrame(productsFrame, text="Pizza", font=("times new roman", 15, "bold"), bg="pink", fg="black", bd=5)
PizzaFrame.grid(row=0, column=0)


#veg pizza block

VegpizzaLabel = Label(PizzaFrame, text="Veg Pizza", font=("times new roman", 15, "bold"), bg="pink",fg="black")
VegpizzaLabel.grid(row=0, column=0, pady=9, padx=10, sticky="w")

VegpizzaEntry = Entry( PizzaFrame, font=("times new roman", 15, "bold"), width=10,bd=5)
VegpizzaEntry.grid(row=0, column=1, pady=9, padx=10)


# paneer pizza block

PaneerpizzaLabel = Label(PizzaFrame, text="Paneer pizza", font=("times new roman", 15, "bold"), bg="pink",fg="black")
PaneerpizzaLabel.grid(row=1, column=0, pady=9, padx=10, sticky="w")

PaneerpizzaEntry = Entry( PizzaFrame, font=("times new roman", 15, "bold"), width=10,bd=5)
PaneerpizzaEntry.grid(row=1, column=1, pady=9, padx=10)

# cheez pizza block

cheezpizzaLabel = Label(PizzaFrame, text="Cheez pizza", font=("times new roman", 15, "bold"), bg="pink",fg="black")
cheezpizzaLabel.grid(row=2, column=0, pady=9, padx=10, sticky="w")

cheezpizzaEntry = Entry( PizzaFrame, font=("times new roman", 15, "bold"), width=10,bd=5)
cheezpizzaEntry.grid(row=2, column=1, pady=9, padx=10)


# italian pizza block
ItalianpizzaLabel = Label(PizzaFrame, text="Italian pizza", font=("times new roman", 15, "bold"), bg="pink",fg="black")
ItalianpizzaLabel.grid(row=3, column=0, pady=9, padx=10, sticky="w")

ItalianpizzaEntry = Entry( PizzaFrame, font=("times new roman", 15, "bold"), width=10,bd=5)
ItalianpizzaEntry.grid(row=3, column=1, pady=9, padx=10)

#Greek pizza
GreekpizzaLabel = Label(PizzaFrame, text="Greek pizza", font=("times new roman", 15, "bold"), bg="pink",fg="black")
GreekpizzaLabel.grid(row=4, column=0, pady=9, padx=10, sticky="w")

GreekpizzaEntry = Entry( PizzaFrame, font=("times new roman", 15, "bold"), width=10,bd=5)
GreekpizzaEntry.grid(row=4, column=1, pady=9, padx=10)


#Margherita pizza

MargeritapizzaLabel = Label(PizzaFrame, text="Margerita pizza", font=("times new roman", 15, "bold"), bg="pink",fg="black")
MargeritapizzaLabel.grid(row=5, column=0, pady=9, padx=10, sticky="w")

MargeritapizzaEntry = Entry( PizzaFrame, font=("times new roman", 15, "bold"), width=10,bd=5)
MargeritapizzaEntry.grid(row=5, column=1, pady=9, padx=10)



# momos div
momosFrame = LabelFrame(productsFrame, text="Momos", font=("times new roman", 15, "bold"), bg="pink", fg="black", bd=5)
momosFrame.grid(row=0, column=1)


# steamvegmomos div
SteamVegmomosLabel = Label(momosFrame, text="Steam veg", font=("times new roman", 15, "bold"), bg="pink",fg="black")
SteamVegmomosLabel.grid(row=0, column=0, pady=9, padx=10, sticky="w")

SteamVegmomosEntry = Entry( momosFrame, font=("times new roman", 15, "bold"), width=10,bd=5)
SteamVegmomosEntry.grid(row=0, column=1, pady=9, padx=10)


# friedvegmomos div
FriedVegmomosLabel = Label(momosFrame, text="fried veg", font=("times new roman", 15, "bold"), bg="pink",fg="black")
FriedVegmomosLabel.grid(row=1, column=0, pady=9, padx=10, sticky="w")

FriedVegmomosEntry = Entry( momosFrame, font=("times new roman", 15, "bold"), width=10,bd=5)
FriedVegmomosEntry.grid(row=1, column=1, pady=9, padx=10)


#steampaneermomos div
SteampaneermomosLabel = Label(momosFrame, text="Steam paneer", font=("times new roman", 15, "bold"), bg="pink",fg="black")
SteampaneermomosLabel.grid(row=2, column=0, pady=9, padx=10, sticky="w")

SteampaneermomosEntry = Entry( momosFrame, font=("times new roman", 15, "bold"), width=10,bd=5)
SteampaneermomosEntry.grid(row=2, column=1, pady=9, padx=10)


#friedpaneermomos div
FriedpaneermomosLabel = Label(momosFrame, text="Fried paneer", font=("times new roman", 15, "bold"), bg="pink",fg="black")
FriedpaneermomosLabel.grid(row=3, column=0, pady=9, padx=10, sticky="w")

FriedpaneermomosEntry = Entry( momosFrame, font=("times new roman", 15, "bold"), width=10,bd=5)
FriedpaneermomosEntry.grid(row=3, column=1, pady=9, padx=10)


#chickenmomos div
ChickenmomosLabel = Label(momosFrame, text="Chicken", font=("times new roman", 15, "bold"), bg="pink",fg="black")
ChickenmomosLabel.grid(row=4, column=0, pady=9, padx=10, sticky="w")

ChickenmomosEntry = Entry( momosFrame, font=("times new roman", 15, "bold"), width=10,bd=5)
ChickenmomosEntry.grid(row=4, column=1, pady=9, padx=10)


#chillimomos div
ChillimomosLabel = Label(momosFrame, text="Chilli", font=("times new roman", 15, "bold"), bg="pink",fg="black")
ChillimomosLabel.grid(row=5, column=0, pady=9, padx=10, sticky="w")

ChillimomosEntry = Entry( momosFrame, font=("times new roman", 15, "bold"), width=10,bd=5)
ChillimomosEntry.grid(row=5, column=1, pady=9, padx=10)



# Combo div
ComboFrame = LabelFrame(productsFrame, text="Combo", font=("times new roman", 15, "bold"), bg="pink", fg="black", bd=5)
ComboFrame.grid(row=0, column=2)

#Burger div
BurgerLabel = Label(ComboFrame, text="Burger", font=("times new roman", 15, "bold"), bg="pink",fg="black")
BurgerLabel.grid(row=0, column=0, pady=9, padx=10, sticky="w")

BurgerEntry = Entry( ComboFrame, font=("times new roman", 15, "bold"), width=10,bd=5)
BurgerEntry.grid(row=0, column=1, pady=9, padx=10)

#sandwich
SandwichLabel = Label(ComboFrame, text="Sandwich", font=("times new roman", 15, "bold"), bg="pink",fg="black")
SandwichLabel.grid(row=1, column=0, pady=9, padx=10, sticky="w")

SandwichEntry = Entry( ComboFrame, font=("times new roman", 15, "bold"), width=10,bd=5)
SandwichEntry.grid(row=1, column=1, pady=9, padx=10)

#cachori
CachoriLabel = Label(ComboFrame, text="Cachori", font=("times new roman", 15, "bold"), bg="pink",fg="black")
CachoriLabel.grid(row=2, column=0, pady=9, padx=10, sticky="w")

CachoriEntry = Entry( ComboFrame, font=("times new roman", 15, "bold"), width=10,bd=5)
CachoriEntry.grid(row=2, column=1, pady=9, padx=10)

#cold coffe
ColdcofeeLabel = Label(ComboFrame, text="Cold Cofee", font=("times new roman", 15, "bold"), bg="pink",fg="black")
ColdcofeeLabel.grid(row=3, column=0, pady=9, padx=10, sticky="w")

ColdcofeeEntry = Entry( ComboFrame, font=("times new roman", 15, "bold"), width=10,bd=5)
ColdcofeeEntry.grid(row=3, column=1, pady=9, padx=10)

#machurian

ManchurianLabel = Label(ComboFrame, text="Manchurian", font=("times new roman", 15, "bold"), bg="pink",fg="black")
ManchurianLabel.grid(row=4, column=0, pady=9, padx=10, sticky="w")

ManchurianEntry = Entry( ComboFrame, font=("times new roman", 15, "bold"), width=10,bd=5)
ManchurianEntry.grid(row=4, column=1, pady=9, padx=10)

# noodles
NoodlesLabel = Label(ComboFrame, text="Noodles", font=("times new roman", 15, "bold"), bg="pink",fg="black")
NoodlesLabel.grid(row=5, column=0, pady=9, padx=10, sticky="w")

NoodlesEntry = Entry( ComboFrame, font=("times new roman", 15, "bold"), width=10,bd=5)
NoodlesEntry.grid(row=5, column=1, pady=9, padx=10)


# bill frame

billframe = Frame(productsFrame, bd=8,relief=GROOVE)
billframe.grid(row=0, column=3,padx=10)

billareaLabel = Label(billframe, text="Bill Area", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="hot pink")
billareaLabel.pack(fill=X)


scrollbar= Scrollbar(billframe, orient=VERTICAL)
scrollbar.pack(side= RIGHT, fill=Y)
textarea = Text(billframe, height=18, width=60, yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)



# bill menu div
billmenuFrame = LabelFrame(root, text="bill menu", font=("times new roman", 15, "bold"), bg="pink", fg="black", bd=5)
billmenuFrame.pack()


pizaaprizeLabel = Label(billmenuFrame, text="Pizza price", font=("times new roman", 15 , "bold"),bg="pink", fg="black") 
pizaaprizeLabel.grid(row=0, column=0, pady=9, padx=10,sticky="w")

pizaaprizeEntry = Entry(billmenuFrame, font=("times new roman",15,"bold"), width=10,bd=5)
pizaaprizeEntry.grid(row=0, column=1, pady=9, padx=10)


pizaaprizeLabel = Label(billmenuFrame, text="Pizza tax", font=("times new roman", 15 , "bold"),bg="pink", fg="black") 
pizaaprizeLabel.grid(row=0, column=2, pady=9, padx=10,sticky="w")

pizaaprizeEntry = Entry(billmenuFrame, font=("times new roman",15,"bold"), width=10,bd=5)
pizaaprizeEntry.grid(row=0, column=3, pady=9, padx=10)





momosprizeLabel = Label(billmenuFrame, text="Momos price", font=("times new roman", 15 , "bold"),bg="pink", fg="black") 
momosprizeLabel.grid(row=1, column=0, pady=9, padx=10,sticky="w")

momosprizeEntry = Entry(billmenuFrame, font=("times new roman",15,"bold"), width=10,bd=5)
momosprizeEntry.grid(row=1, column=1, pady=9, padx=10)

momosprizeLabel = Label(billmenuFrame, text="Momos tax", font=("times new roman", 15 , "bold"),bg="pink", fg="black") 
momosprizeLabel.grid(row=1, column=2, pady=9, padx=10,sticky="w")

momosprizeEntry = Entry(billmenuFrame, font=("times new roman",15,"bold"), width=10,bd=5)
momosprizeEntry.grid(row=1, column=3, pady=9, padx=10)





comboprizeLabel = Label(billmenuFrame, text="Combo price", font=("times new roman", 15 , "bold"),bg="pink", fg="black") 
comboprizeLabel.grid(row=2, column=0, pady=9, padx=10,sticky="w")

comboprizeEntry = Entry(billmenuFrame, font=("times new roman",15,"bold"), width=10,bd=5)
comboprizeEntry.grid(row=2, column=1, pady=9, padx=10)


comboprizeLabel = Label(billmenuFrame, text="Combo tax", font=("times new roman", 15 , "bold"),bg="pink", fg="black") 
comboprizeLabel.grid(row=2, column=2, pady=9, padx=10,sticky="w")

comboprizeEntry = Entry(billmenuFrame, font=("times new roman",15,"bold"), width=10,bd=5)
comboprizeEntry.grid(row=2, column=3, pady=9, padx=10)



ButtonFrame = Frame(billmenuFrame, bd=8, relief=GROOVE)
ButtonFrame.grid(row=0, column=4, rowspan=3)


totalButton = Button(ButtonFrame, text="Total", font=("arial", 16, "bold"), bg="hot pink", fg="black", width=8, pady=10, )
totalButton.grid(row=0, column=0, pady=20, padx=5)

billButton = Button(ButtonFrame, text="Bill", font=("arial", 16, "bold"), bg="hot pink", fg="black", width=8, pady=10)
billButton.grid(row=0, column=1, pady=20, padx=5)

emailButton = Button(ButtonFrame, text="Email", font=("arial", 16, "bold"), bg="hot pink", fg="black", width=8, pady=10, )
emailButton.grid(row=0, column=2, pady=20, padx=5)

printButton = Button(ButtonFrame, text="Print", font=("arial", 16, "bold"), bg="hot pink", fg="black", width=8, pady=10, )
printButton.grid(row=0, column=3, pady=20, padx=5)

clearButton = Button(ButtonFrame, text="Clear", font=("arial", 16, "bold"), bg="hot pink", fg="black", width=8, pady=10, command=clear_fields)
clearButton.grid(row=0, column=4, pady=20, padx=5)

root.mainloop()
