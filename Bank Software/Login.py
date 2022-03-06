from tkinter import *
from tkinter import filedialog
root=Tk()
root.geometry("300x200")
def getvals():
    print("Accepted")
#Heading
Label(root,text="---Login Form---" , font="ar 15 bold").grid(row=0,column=3)
#Fields Names 
Login= Label(root, text="Username:")
Password=Label(root,text="Password:")
#Packing Fields
Login.grid(row=1,column=2)
Password.grid(row=2,column=2)
#Variables For Storing Data
Loginvalue=StringVar
Passwordvalue=IntVar
#Variable Entry Field
Loginentry= Entry(root,textvariable =Loginvalue)
Passwordentry= Entry(root,textvariable =Passwordvalue)
#Adding Grid to it
Loginentry.grid(row=1,column=3)
Passwordentry.grid(row=2,column=3)
root.mainloop()