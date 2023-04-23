from tkinter import *

window = Tk()

window.title("Chelsea FC Contract Agreement")
icon = PhotoImage(file = "Chelsea.png")
window.iconphoto(True, icon)

photo = PhotoImage(file= "Chelsea.png")

label = Label(window,
text = "Contract Agreement \n \n ",
font= ("SF Pro Display",20),
image= photo,
compound= TOP
)

label.pack()

label1 = Label(window,
text= " Player Name: Sofonias Alemayehu \n Team Name: Chelsea Football Club\n Contract Duration: 5 years\n Base Salary: £3.4 million per year\n Signing Bonus: £50,000\n *£5,000 bonus for every hat trick scored \n *£20,000 bonus for every trophy won\n *£25,000 bonus for every goal scored in a cup final\n \n ",
justify= LEFT,
font=("SF Pro Display", 15))

label1.pack()

check = Checkbutton(window,text="I accept the terms and conditions", font=("SF Pro Display",17), justify=CENTER)

check.pack()

check1 = Checkbutton(window,text="I do not accept the terms and conditions", font=("SF Pro Display",17), justify=CENTER)

check1.pack()

window.mainloop()