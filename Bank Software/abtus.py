from tkinter import *
import tkinter
import webbrowser


# creating Tk window
root = Tk()
root.geometry('2000x2000')
frame1 = Frame(root, background='skyblue', height=100, width=100,pady=30)


title=Label(frame1, text="", font=('Helvetica 48 bold'),padx=50,pady=40, bg='skyblue')

img=tkinter.PhotoImage(file=r"C:\Users\ SANAT RUNWAL\ Desktop\ Bank Software\logo.png")
photoimage = img.subsample(15, 15)

label = Label(frame1, image = photoimage,padx=10,pady=30,bg='skyblue')

Login= Button(frame1,text="Login",font=('Helvetica 17 bold'),bg='skyblue',border='1')
Register=Button(frame1,text="Register",font=('Helvetica 17 bold'),bg='skyblue',border='1')

homeBtn= Button(frame1,text="Home",font=('Helvetica 17 bold'),bg='skyblue',border='0',padx=10,pady=5)
aboutBtn= Button(frame1,text="About Us",font=('Helvetica 17 bold'),bg='skyblue',border='0')
contactBtn= Button(frame1,text="Contact Us",font=('Helvetica 17 bold'),bg='skyblue',border='0')

frame1.place(expand=False,fill='x')

lbl=Label(root, text="About Us", font=('Helvetica 30 bold'))
lbl.pack(side=TOP)

abtcntnt=Label(root, text="We’re just the bank you need.\n Banking with passion for 25+years Established by Hon. Shri Baburao Kanpade, former Member of Parliament,\n"
                          "on 4th April 1996, Ula-Dhal Bank Ltd., a Primary Urban Co-op Bank,\n"
                          "in Nagpur is registered under the Co-op Societies Act 1960 and is licensed by RBI.\n "
                          "Our Board consists of 17 directors, two of them being Chartered Accountants with rich \n"
                          "experience in banking and audit. \n\n Currently,the bank is working under the leadership of Chairman Shri Nana Chormare.\n"
                          "With our swift financial services and quick response to queries/complaints, it didn’t take long \n "
                          "for us to gain the trust of our customers and stakeholders."
                          "\n\n Today, we stand shoulder to shoulder with the leading and best performing banks in the Co-op Banking Sector.\n"
                          "While our area of operation extends across the entire state of Maharashtra, we have a total of 16 branches,\n"
                          "13 in the city of Nagpur and one each at Wardha, Airoli (New Mumbai), and Chandrapur. Our state-of-the-art branches \n "
                          "ensure customers get a hassle-free banking experience around the week.The Bank is rated as ‘A’ grade in Audits."
                          "\n\nThe Bank is a member of Deposit Insurance & Credit Guarantee Corporation, and such deposits of the customers \n"
                          "are secured to the extent of Rs 5 lakh, as per the DICGC scheme.\n ", font=('Helvetica 15'))
abtcntnt.pack(side=TOP,padx=10,pady=10)
label.pack(side=LEFT)

title.pack(side=LEFT)
Register.place(x=1320,y=30)
Login.place(x=1230,y=30)
contactBtn.place(x=1380,y=130)
aboutBtn.place(x=1230,y=130)
homeBtn.place(x=1100,y=126)


def callback(url):
    webbrowser.open_new(url)
homeBtn.bind("<Button-1>", lambda e: callback(r"C:\Users\\SANAT RUNWAL\\Desktop\\Bank Software\\Bank Software\homepage.py"))
aboutBtn.bind("<Button-1>", lambda e: callback(r"C:\Users\\SANAT RUNWAL\\Desktop\\Bank Software\abtus.py"))
contactBtn.bind("<Button-1>", lambda e: callback(r"C:\Users\TEJAS\Desktop\Python\Bank\contactUs.py"))

root.mainloop()
