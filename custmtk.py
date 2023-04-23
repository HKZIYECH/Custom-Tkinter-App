import customtkinter 
import tkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

window = customtkinter.CTk()

window.title("AIS Regsitration")
window.geometry("720x480")

#TITLE
label = customtkinter.CTkLabel(window, text="AIS Registration Form\n", font=("SF Pro Display",40))

label.pack()


#FRAME
frame = customtkinter.CTkFrame(window)

frame.pack(pady=10, padx=20, expand=True, fill="both")


#FIRST NAME

firstName = customtkinter.CTkLabel(frame, text="First Name", font=("Roboto",20))

firstName.place(relx=0, rely=0.1)

fname = customtkinter.CTkEntry(frame, placeholder_text="Enter your first name", font=("calibri",14), width=200)
fname.place(relx=0.3,rely=0.1)
 
 #LAST NAME

secondName = customtkinter.CTkLabel(frame, text="Last Name", font=("Roboto",20))

secondName.place(relx=0, rely=0.2)

lname = customtkinter.CTkEntry(frame, placeholder_text="Enter your last name", font=("calibri",15), width=200)
lname.place(relx=0.3,rely=0.2)

#GRADE

grade= customtkinter.CTkLabel(frame, text="Grade", font=("SF Pro Display",20))
grade.place(relx= 0, rely=0.3)

gent = customtkinter.CTkEntry(frame, placeholder_text="Enter Your Grade", font=("Calibri",14), width=200)
gent.place(relx= 0.3, rely=0.3)

#AGE

age= customtkinter.CTkLabel(frame, text="Age", font=("SF Pro Display",20))
age.place(relx= 0, rely=0.4)

aent = customtkinter.CTkEntry(frame, placeholder_text="Enter Your Age", font=("Calibri",14), width=200)
aent.place(relx= 0.3, rely=0.4)

#GENDER

gender= customtkinter.CTkLabel(frame, text="Gender", font=("SF Pro Display",20))
gender.place(relx= 0, rely=0.5)

gdent = customtkinter.CTkEntry(frame, placeholder_text="Enter Your Gender", font=("Calibri",14), width=200)
gdent.place(relx= 0.3, rely=0.5)

#EMAIL

email= customtkinter.CTkLabel(frame, text="Email", font=("SF Pro Display",20))
email.place(relx= 0, rely=0.6)

gdent = customtkinter.CTkEntry(frame, placeholder_text="Enter Your Email", font=("Calibri",14), width=200)
gdent.place(relx= 0.3, rely=0.6)

#MINISTRY

ministry = customtkinter.CTkCheckBox(frame, text="I have taken grade 8 ministry exam", font=("SF Pro Display",14))

ministry.place(relx= 0, rely=0.7)

#TRANSCRIPT

transcript = customtkinter.CTkCheckBox(frame, text="I have my official transcript", font=("SF Pro Display",14))

transcript.place(relx= 0, rely=0.8)

#SUBMIT

button = customtkinter.CTkButton(frame, text="Submit", font=("SF Pro Display",17))
button.place(relx=0.35, rely=0.90)

padding = customtkinter.CTkLabel(frame, text="\n")
padding.place(relx=0, rely= 1)

window.mainloop()