import tkinter
from tkinter import *

root= Tk()
root.title("My To-Do_List")
root.geometry("1180x600+400+100")


task_list= []

def addTask():
    task= task_entry.get()
    task_entry.delete(0,END)

    if task:
       with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
       task_list.append(task)
       listbox.insert( END,task)

def deleteTask():
    global task_list
    task =str(listbox.get(ANCHOR))
    if task in task_list:
        task_list .remove(task)
        with open ("tasklist.txt", 'w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")

        listbox.delete( ANCHOR)


def openTaskFile():
    try:
        global task_list
    
        with open("tasklist.txt","r") as taskfile:
         
            tasks= taskfile.readlines()

        for task in tasks:
            if task !='\n':
               task_list.append(task)
               listbox.insert(END,task)

    except:
     file=open('tasklist.txt', 'w')
     file.close()

#icon
Image_icon=PhotoImage(file="Image/task.png")
root.iconphoto(False,Image_icon)


#top bar
TopImage=PhotoImage(file="Image/top.png")
Label(root,image=TopImage).pack()

dockImage=PhotoImage(file="Image/duck.png")
Label(root, image=dockImage, bg="#dae4e6").place(x=30,y=25)


noteImage=PhotoImage(file="Image/task.png")
Label(root,image=noteImage, bg= "#dae4e6").place(x=1070,y=25)

heading=Label(root,text="ALL TASK", font="arial 50 bold", fg="Black", bg="#dae4e6")
heading.place(x=400,y=20)

#main
frame= Frame(root, width=400, height=50, bg="#dae4e6")
frame.place(x=400,y=180)

task= StringVar()
task_entry=Entry(frame,width=18,font="arial 20", bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()


button=Button(frame,text="ADD", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0, command=addTask)
button.place(x=300, y=0)

#listbox
frame1= Frame(root, bd=3, width=400, height=300, bg="#dae4e6")
frame1.place(x=360,y=250)

listbox= Listbox(frame1,font=('arial',15),width=60, height=11,bg= "#01061a", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)

scrollbar= Scrollbar(frame1)
scrollbar.pack(side= RIGHT, fill= BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

#delete
Delete_icon=PhotoImage(file="Image/delete.png")
Button(root,image=Delete_icon,bd=0, command=deleteTask).pack(side=BOTTOM, pady=13)




















                 

root.mainloop()
