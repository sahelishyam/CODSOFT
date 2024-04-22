from tkinter import *
import random
import string
from tkinter.ttk import Combobox
root1=Tk()
root1.geometry("400x200")
root1.title("ROCK vs PAPER vs SCISSORS Game")
root1.resizable(False,False)
root1.config(bg="#97FFFF")
label_rule= Label(root1,text="Game Winning Rules:",font=("arial",20,"bold"),fg="red4",bg="#97FFFF")
label_rule.pack(pady=5)
label_rule1= Label(root1,text="Rule1: Rock beats Scissors",font=("arial",12,"bold"),bg="#97FFFF")
label_rule1.pack(pady=10)
label_rule2= Label(root1,text="Rule2: Scissors beats Paper",font=("arial",12,"bold"),bg="#97FFFF")
label_rule2.pack(pady=5)
label_rule3= Label(root1,text="Rule3: Paper beats Rock \t",font=("arial",12,"bold"),bg="#97FFFF")
label_rule3.pack(pady=5)
score_user=0
score_computer=0
def start():
   root2=Tk()
   root2.geometry("400x500")
   root2.title("ROCK vs PAPER vs SCISSORS Game")
   root2.resizable(False,False)
   root2.config(bg="#97FFFF") 
   label_us= Label(root2,text="Player's Choice",font=("arial",18,"bold"),bg="#97FFFF")
   label_us.pack(pady=5)
   choice=IntVar()
   ll=["Rock","Paper","Scissor"]
   s=0
   def choice(t):
       global s
       global p
       if t==1:
           s=1
           label_userchoice.config(text="Rock")
       if t==2:
           s=2
           label_userchoice.config(text="Paper")
       if t==3:
           s=3
           label_userchoice.config(text="Scissor")
       p=str(random.choice(ll))
       label_computerchoice.config(text=p)
       
           
   def clear():
       global p
       p=""
       label_result.config(text="")
       label_computerchoice.config(text="")
       label_userchoice.config(text="")
       
   p=StringVar()
   p=""
   win=""
   c=0
   
   def play():
       global win
       global p
       global c
       global s
       global score_user
       global score_computer
       if p=="Rock":
           c=1
       elif p=="Paper":
           c=2
       elif p=="Scissor":
           c=3
       if c==3 and s==1:
           win="the winner is Player"
           score_user=score_user + 1
       elif c==1 and s==3:
           win="the winner is computer"
           score_computer=score_computer + 1
       elif c<s:
           win="the winner is Player"
           score_user=score_user + 1
       elif c>s:
           win="the winner is computer"
           score_computer=score_computer + 1
       else:
           win="It's a Tie"
       label_result.config(text=win)
       trs="Player's Score:" + str(score_user) + "\t Computer's score:" + str(score_computer)
       label_score.config(text=trs)

   Button(root2,text="Rock",width=12,height=1,font=("arial",10,"bold"),bd=1,bg="#0000FF",fg="#fff",command=lambda:choice(1)).place(x=40,y=50)
   Button(root2,text="Paper",width=12,height=1,font=("arial",10,"bold"),bd=1,bg="#0000FF",fg="#fff",command=lambda:choice(2)).place(x=160,y=50)
   Button(root2,text="Scissor",width=12,height=1,font=("arial",10,"bold"),bd=1,bg="#0000FF",fg="#fff",command=lambda:choice(3)).place(x=280,y=50)
   label_userchoice= Label(root2,width=15,height=1,text="",font=("arial",15),fg="red4")
   label_userchoice.pack(pady=35)
   label_vs=Label (root2,text="Vs",font=("arial",20,"bold"),bg="#97FFFF",fg="red4").place(x=180,y=110)
   label_comp= Label(root2,text="Computer's Choice",font=("arial",18,"bold"),bg="#97FFFF")
   label_comp.pack()
   label_computerchoice= Label(root2,width=25,height=1,text="",font=("arial",15),fg="red4")
   label_computerchoice.pack(pady=10)
   label_result= Label(root2,width=40,height=1,text="",font=("arial",15,"bold"),fg="#006400")
   label_result.pack(pady=15)
   
   Button(root2,width=8,height=1,font=(8),bd=1,bg="#0000FF",fg="#fff",text="play",command=lambda:play()).place(x=160,y=300) 
   label_s= Label(root2,text="Score:",font=("arial",17,"bold"),fg="red4",bg="#97FFFF").place(x=20,y=310)
   label_score= Label(root2,width=30,height=1,font=("arial",12,"bold"),text="user: \t computer:")
   label_score.pack(pady=60)
   
   Button(root2,text="Play Again",width=12,height=1,font=("arial",10,"bold"),bd=1,bg="red4",fg="#fff",command=lambda:clear()).place(x=290,y=450)    
Button(root1,text="Start Game",width=10,height=1,font=("arial",10,"bold"),bd=1,fg="#fff",bg="#0000FF",command=lambda:start()).place(x=300,y=150)
root1.mainloop()
