from tkinter import *
root=Tk()
root.title("CALCULATOR")
root.geometry("570x570")
root.resizable(False,False)
root.configure(bg="#97FFFF")
h=""
equation=""
def show(value):
    global h
    global equation
    equation+=value
    label_result.config(text=equation)

def clear():
    global equation
    equation=""
    label_result.config(text=equation)
    global h
    h=""
def calculate():
    global equation
    result=""
    if equation!="":
        try:
            result=eval(equation)
        except:
            result="error"
            equation=""
    label_result.config(text=result)
    global h
    h=str(result)
    equation=h
def cross():
    global equation
    x=list(equation)
    x.pop()
    equation=""
    for ele in x:
     equation+=ele
    label_result.config(text=equation)

    
label_result= Label(root,width=570,height=2,text="",font=("arial",30))
label_result.pack()
Button(root,text="c",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#FF83FA",command=lambda:clear()).place(x=10,y=100)
Button(root,text="/",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#FF83FA",command=lambda:show("/")).place(x=150,y=100)
Button(root,text="*",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#FF83FA",command=lambda:show("*")).place(x=290,y=100)
Button(root,text="%",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#FF83FA",command=lambda:show("%")).place(x=430,y=100)

Button(root,text="7",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:show("7")).place(x=10,y=190)
Button(root,text="8",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:show("8")).place(x=150,y=190)
Button(root,text="9",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:show("9")).place(x=290,y=190)
Button(root,text="+",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#FF83FA",command=lambda:show("+")).place(x=430,y=190)

Button(root,text="4",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:show("4")).place(x=10,y=280)
Button(root,text="5",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:show("5")).place(x=150,y=280)
Button(root,text="6",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:show("6")).place(x=290,y=280)
Button(root,text="-",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#FF83FA",command=lambda:show("-")).place(x=430,y=280)

Button(root,text="1",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:show("1")).place(x=10,y=370)
Button(root,text="2",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:show("2")).place(x=150,y=370)
Button(root,text="3",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:show("3")).place(x=290,y=370)
Button(root,text="=",width=5,height=3,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#C71585",command=lambda:calculate()).place(x=430,y=370)

Button(root,text="0",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:show("0")).place(x=10,y=460)
Button(root,text=".",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:show(".")).place(x=150,y=460)
Button(root,text="X",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:cross()).place(x=290,y=460)

root.mainloop()
