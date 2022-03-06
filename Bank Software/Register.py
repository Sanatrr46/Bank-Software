from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from turtle import colormode
import pandas as pd
import numpy as np
import os, shutil

root = Tk()
root.geometry("500x300")

def getvals():
    print("Accepted")
#Heading
Label(root,text="---Registration Form---" , font="ar 15 bold").grid(row=0,column=3)


#Field Name
name= Label(root, text="Name:")
phone=Label(root,text="Phone:")
gender=Label(root,text="Gender:")
address= Label(root, text="Address:")
gmail=Label(root,text="Gmail ID:")
password=Label(root,text="Password:")
confirmpassword=Label(root,text="Confirm Password:")
#Packing Fields 
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
address.grid(row=4,column=2)
gmail.grid(row=5,column=2)
password.grid(row=6,column=2)
confirmpassword.grid(row=7,column=2)
#Variables For Storing Data
namevalue=StringVar
phonevalue=IntVar
gendervalue=Radiobutton
addressvalue=StringVar
gmailvalue=StringVar
character=IntVar
passwordvalue=IntVar
confirmpasswordvalue=IntVar
#Variable Entry Field
nameentry= Entry(root,textvariable =namevalue)
phoneentry= Entry(root,textvariable =phonevalue)
genderentry=Entry(root,textvariable =gendervalue)
addressentry= Entry(root,textvariable =addressvalue)
gmailentry= Entry(root,textvariable =gmailvalue)
passwordentry=Entry(root,textvariable=passwordvalue)
confirmpasswordentry=Entry(root,textvariable=confirmpasswordvalue)
#Adding Grid to it
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)

addressentry.grid(row=4,column=3)
gmailentry.grid(row=5,column=3)
passwordentry.grid(row=6,column=3)
confirmpassword.grid(row=7,column=3)
#Creating Check box
checkbtn=Radiobutton(text="Male",variable = character ,value=1)
checkbtn.grid(row=3,column=3)
checkbtn2=Radiobutton(text="Female",variable = character,value=1)
checkbtn2.grid(row=3,column=4)
checkbtn3=Radiobutton(text="Other",variable = character,value=1)
checkbtn3.grid(row=3,column=5)
#Submit Button
Button(text="Submit",command=getvals).grid(row=9 ,column=3)

root.mainloop()