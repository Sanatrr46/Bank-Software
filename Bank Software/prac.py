from tkinter import *
from PIL import ImageTK,Image

root=Tk()
root.title('HI')
root.geometry("400x400")
def show():
    myLabel = Label(root,text=clicked.get()).pack()

options =["Male",
        "Female",
        "Other"]    
clicked=StringVar()
clicked.set(options[0])
drop=OptionMenu(root,clicked,"Male","Female","Other").grid(row=3,column=5)
drop.pack()



myButton=Button(root,text="Show Selection", command=show).pack()

root.mainloop()