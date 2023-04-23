#Button Part

photo = PhotoImage(file = "icon.png")
button = Button(window,
text= "Check Weather",
command= btn,
font = ('SF Pro Display',20),
bg = "white",
fg = "#000000",
activeforeground = "#fff70f",
activebackground = "light blue",
image= photo,
compound= BOTTOM)

button.pack()