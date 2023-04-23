import tkinter
import customtkinter
from pytube import YouTube

#Function

def startDownload():
    try:
        ytLink = input.get()
        ytObject = YouTube(ytLink)
        video= ytObject.streams.get_highest_resolution()
        video.download()
    except:
        print("YouTube link is invalid")
    print("Download Complete!")

#Theme and Appearance

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

#Dimensions and Frame

window = customtkinter.CTk()
window.geometry("720x480")
window.title("YouTube Video Downloader")

#Main Code

title = customtkinter.CTkLabel(window, text="YouTube video downloader", font=("SF Pro Display",40))
title.pack()

url_var = tkinter.StringVar()

input = customtkinter.CTkEntry(window, placeholder_text="Enter Video Link", font=("Calibri",20), width=350, height=40, textvariable=url_var)
input.pack(padx=10,pady=10)

button = customtkinter.CTkButton(window, text="Download", font=("SF Pro Display",15), command=startDownload)
button.pack()

#Run Code

window.mainloop()