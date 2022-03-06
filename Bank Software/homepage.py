from distutils import command
from tkinter import *
import tkinter
from turtle import back
import webbrowser


# creating Tk window
root = Tk()
root.geometry('2000x2000')
sb=Scrollbar(root)
sb.pack(side = RIGHT, fill = Y)

frame1 = Frame(root, background='skyblue', height=100, width=100,pady=5)


title=Label(frame1, text="True Finance", font=('Helvetica 48 bold'),padx=50,pady=40, bg='skyblue')

img = tkinter.PhotoImage(file=r"\Users\\SANAT RUNWAL\\Desktop\\Bank Software\\Bank Software\logo.png")
photoimage = img.subsample(15, 15)

label = Label(frame1, image = photoimage,padx=10,pady=30,bg='skyblue')

Login= Button(frame1,text="Login",font=('Helvetica 17 bold'),bg='skyblue',border='1')
Register=Button(frame1,text="Register",font=('Helvetica 17 bold'),bg='skyblue',border='1')

homeBtn= Button(frame1,text="Home",font=('Helvetica 17 bold'),bg='skyblue',border='0')
aboutBtn= Button(frame1,text="About Us",font=('Helvetica 17 bold'),bg='skyblue',border='0')
contactBtn= Button(frame1,text="Contact Us",font=('Helvetica 17 bold'),bg='skyblue',border='0')

frame2= Frame(root,height=150,width=150,pady=80, background='white')
frame3= Frame(root,height=150,width=150,pady=80, background='white')
frame4= Frame(root,height=150,width=150,pady=80, background='white')
frame5= Frame(root,height=150,width=150,pady=80, background='white')
frame6= Frame(root,height=615,width=1363,pady=80, background='white')



EmiCalci=Button(frame5,text="EMI Calculator",font=('Helvetica 12 bold'),bg='skyblue',border='1')
EmiCalci.place(x=15,y=23)

emiimg = tkinter.PhotoImage(file=r"C:\Users\\SANAT RUNWAL\\Desktop\\Bank Software\\Bank Software\emiCalci.png")
EMIphotoimage = emiimg.subsample(6, 6)
EMIlabel = Label(frame5, image = EMIphotoimage,padx=10,pady=30,bg='white')
EMIlabel.place(x=38,y=-67)


Transferimg = tkinter.PhotoImage(file=r"C:\Users\\SANAT RUNWAL\\Desktop\\Bank Software\\Bank Software\transferMoney.png")
Transferphotoimage = Transferimg.subsample(4, 4)
Transferlabel = Label(frame4, image = Transferphotoimage,padx=10,pady=30,bg='white')
Transferlabel.place(x=12,y=-87)

TransferBtn=Button(frame4,text="Transfer Money",font=('Helvetica 12 bold'),bg='skyblue',border='1')
TransferBtn.place(x=11,y=23)

frame1.pack(expand=False,fill='x')
label.pack(side=LEFT)
title.pack(side=LEFT)

Register.place(x=1320,y=30)
Login.place(x=1230,y=30)
contactBtn.place(x=1380,y=110)
aboutBtn.place(x=1230,y=110)
homeBtn.place(x=1100,y=110)

frame5.place(x=5,y=640)
frame4.place(x=5,y=485)
frame3.place(x=5,y=330)
frame2.place(x=5,y=175)
frame6.place(x=160,y=175)

def callback(url):
    webbrowser.open_new(url)
homeBtn.bind("<Button-1>", lambda e: callback(r"C:\Users\TEJAS\Desktop\Python\Bank\homepage.py"))
aboutBtn.bind("<Button-1>", lambda e: callback(r"C:\Users\TEJAS\Desktop\Python\Bank\abtus.py"))

contactBtn.bind("<Button-1>", lambda e: callback(r"C:\Users\TEJAS\Desktop\Python\Bank\contactUs.py"))
EmiCalci.bind("<Button-1>", lambda e: callback(r"https://emicalculator.net/"))

root.mainloop()