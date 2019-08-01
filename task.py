
from tkinter import *

btnTxt = "Submit!"
 
def validate_info():
  '''  phone_info = phoneNumber.get()
  phone_info = str(phone_info)
  print(phone_info)
 
  
  print(" User ", phone_info, " has been registered successfully")
 
  phone_entry.delete(0, END)'''

  try:
    phone_info = phoneNumber.get()
    phone_info = str(phone_info)

    if len(phone_info) == 10:
      btn = Button(screen,text = "Valid! Please refresh!", width = "30", height = "2", bg = "grey")
      btn.place(x = 15, y = 290)
    else:
      btn = Button(screen,text = "Invalid! Please refresh!", width = "30", height = "2", bg = "grey")
      btn.place(x = 15, y = 290)
  except:
    btn = Button(screen,text = "Invalid! Please refresh!", width = "30", height = "2", bg = "grey")
    btn.place(x = 15, y = 290)





screen = Tk()
screen.geometry("500x500")
screen.title("Phone Number Validation")
heading = Label(text = "Phone Number Validation", bg = "grey", fg = "black", width = "500", height = "3")
heading.pack()
  
phone_text = Label(text = "Phone Number: ",)
phone_text.place(x = 15, y = 70)

phoneNumber = IntVar()
 
phone_entry = Entry(textvariable = phoneNumber, width = "30")
 
phone_entry.place(x = 15, y = 100)
 
btn = Button(screen,text = "Submit", width = "30", height = "2", command = validate_info, bg = "grey")
btn.place(x = 15, y = 290)


screen.mainloop()