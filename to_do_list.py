# we have to create a txt file in our current location where we can store our task list


from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("TO-DO-LIST")
root.geometry("400x500")
root.resizable(False,False)
root.config(bg="gray44")

def add_task():
    task=task_entry.get()
    if task:
        task_list.insert(0,task)
        task_entry.delete(0,END)
        save_task()
    else:
        messagebox.showerror("Error","Enter a Task.")
        
def remove_task():
    selected=task_list.curselection()
    if selected:
        task_list.delete(selected[0])
        save_task()
    else:
       messagebox.showerror("Error","choose a Task to delete")
# we have to create a txt file in our current location where we can store our task list
def save_task():
    with open("tasks.txt","w")as f:
        tasks= task_list.get(0,END)
        for task in tasks:
            f.write(task + "\n")

def load_task():
    try:
      with open("tasks.txt","r")as f:
        tasks= f.readlines()
        for task in tasks:
            task_list.insert(0,task.strip())
    except FileNotFoundError:
         pass

title_label=Label(root,text="To-Do-List",font=("times new roman",25,"bold","italic"),fg="black",bg="gray44").place(x=130,y=20)
add_button=Button(root,width=10,height=1,font=("arial",15,"bold"),fg="#fff",text="Add Task",bg="#06911f",command=add_task).place(x=40,y=80)
add_button=Button(root,width=12,height=1,font=("arial",15,"bold"),fg="#fff",text="Remove Task",bg="red4",command=remove_task).place(x=200,y=80)
task_entry=Entry(root,width=30,font=("arial",15),fg="black")
task_entry.place(x=30,y=150)
task_label=Label(root,text="Tasks",font=("Arial",20,"bold"),fg="red4",bg="gray44").place(x=150,y=190)
task_list=Listbox(root,width=30,height=8,font=("arial",15))
task_list.place(x=30,y=230)
load_task()
root.mainloop()
