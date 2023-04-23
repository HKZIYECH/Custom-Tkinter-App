from tkinter import *

def btn():
  print("Go outside and check")

window = Tk()


window.title("Weather Station")
window.geometry("520x520")
#Text Part

label = Label(window,
  text= "Weather Station",
  font = ('SF Pro Display',20))

label.pack()

#Check Box

check_button = Checkbutton(window,
text= "Fifa 23")

check_button.pack()

window.mainloop()