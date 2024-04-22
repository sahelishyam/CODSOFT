from tkinter import *
import random
import string
root=Tk()
root.geometry("400x400")
root.title("Password Generator App")
root.resizable(False,False)
root.config(bg="#97FFFF")
password=""
def generate():
    small=string.ascii_lowercase
    capital=string.ascii_uppercase
    digit=string.digits
    special=string.punctuation
    a=small+capital+digit+special
    length=va.get()
    if choice.get()==1:
        password=random.sample(small+capital,length)
        label_result.config(text=password,fg="black")
    if choice.get()==2:
        password=random.sample(small+capital+digit,length)
        label_result.config(text=password,fg="black")
    if choice.get()==3:
        password=random.sample(small+capital+digit+special,length)
        label_result.config(text=password,fg="black",font=(20))      

def clear():
     label_result.config(text="please select the complexity and length of the password",fg="red4",font=(12))

label_result= Label(root,width=50,height=4,text="please select the complexity and length of the password",font=("arial",12),fg="red4")
label_result.pack()
Button(root,text="Generate password",width=15,height=1,font=("arial",15,"bold"),bd=1,fg="#fff",bg="#0000FF",command= lambda:generate()).place(x=100,y=100)
label=Label(root,text="Password Complexity:",font=("arial",13,"bold"),bg="#97FFFF").place(x=10,y=150)
choice=IntVar()
r1=Radiobutton(root,text="weak",value=1,variable=choice,font=("arial",15,"bold"),bg="#97FFFF").place(x=188,y=150)
r2=Radiobutton(root,text="medium",value=2,variable=choice,font=("arial",15,"bold"),bg="#97FFFF").place(x=188,y=190)
r3=Radiobutton(root,text="strong",value=3,variable=choice,font=("arial",15,"bold"),bg="#97FFFF").place(x=188,y=230)

label_l=Label (root,text="Password length:",font=("arial",13,"bold"),bg="#97FFFF").place(x=10,y=280)
va=IntVar()
length_box=Spinbox(root,from_=8,to_=16,textvariable=va,width=10,bg="#FFFAF0",font=("arial",15,"bold")).place(x=188,y=300)
Button(root,text="Clear",width=5,height=1,font=("arial",10,"bold"),bd=1,fg="#fff",bg="#0000FF",command=lambda:clear()).place(x=320,y=350)
root.mainloop()
            
