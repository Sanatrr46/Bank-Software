from cgitb import text
from tkinter import *
import tkinter
import webbrowser


# creating Tk window
root = Tk()
root.geometry('2000x2000')

frame1 = Frame(root, background='skyblue', height=100, width=100,pady=30)


title=Label(frame1, text="True Finance", font=('Helvetica 48 bold'),padx=50,pady=40, bg='skyblue')

img = tkinter.PhotoImage(file=r"C:\Users\TEJAS\Desktop\Python\Bank\logo.png")
photoimage = img.subsample(15, 15)

label = Label(frame1, image = photoimage,padx=10,pady=30,bg='skyblue')

Login= Button(frame1,text="Login",font=('Helvetica 17 bold'),bg='skyblue',border='1')
Register=Button(frame1,text="Register",font=('Helvetica 17 bold'),bg='skyblue',border='1')

homeBtn= Button(frame1,text="Home",font=('Helvetica 17 bold'),bg='skyblue',border='0',padx=10,pady=5)
aboutBtn= Button(frame1,text="About Us",font=('Helvetica 17 bold'),bg='skyblue',border='0')
contactBtn= Button(frame1,text="Contact Us",font=('Helvetica 17 bold'),bg='skyblue',border='0')

frame1.pack(expand=False,fill='x')
label.pack(side=LEFT)
title.pack(side=LEFT)

Register.place(x=1320,y=30)
Login.place(x=1230,y=30)
contactBtn.place(x=1380,y=130)
aboutBtn.place(x=1230,y=130)
homeBtn.place(x=1100,y=126)

def callback(url):
    webbrowser.open_new(url)
homeBtn.bind("<Button-1>", lambda e: callback(r"C:\Users\TEJAS\Desktop\Python\Bank\homepage.py"))
aboutBtn.bind("<Button-1>", lambda e: callback(r"C:\Users\TEJAS\Desktop\Python\Bank\aboutUs.py"))
contactBtn.bind("<Button-1>", lambda e: callback(r"C:\Users\TEJAS\Desktop\Python\Bank\contactUs.py"))

contactText=Label(root,text="\nContact Us", font=('Helvetica 40 bold'))
contactText.pack()

contact1=Label(root,text="\n ContactNo.\ Kadam = 8652314596", font=('Helvetica 20 bold'))
contact2=Label(root,text="Vikram = 8656354555\n", font=('Helvetica 20 bold'))
mail=Label(root,text="Mail id\nuladhalbank@gmail.com\n", font=('Helvetica 20 bold'))
address=Label(root,text="Location\nOpposite to Nagaon Beach, Alibaug", font=('Helvetica 20 bold'))

contact1.pack()
contact2.pack()
mail.pack()
address.pack()
root.mainloop()