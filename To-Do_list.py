from tkinter import *
import tkinter.messagebox
import pickle

def add_task():
    task=entry_box.get()
    if task!="":
        listbox.insert(END,task)
        entry_box.delete(0, END)
    else:
        tkinter.messagebox.showwarning(title="warning!!", message="You must enter a task")

def delete_task():
    try:
        index=listbox.curselection()[0]
        listbox.delete(index)
    except:
        tkinter.messagebox.showwarning(title="warning!!", message="You must select a task")

def view_tasks():
    tasks = listbox.get(0, END)
    if tasks:
        task_list = "\n".join(tasks)
        tkinter.messagebox.showinfo("Task List", "Tasks:\n" + task_list)
    else:
        tkinter.messagebox.showinfo("Task List", "No tasks to display.")


def save_tasks():
    tasks = listbox.get(0, listbox.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))
def load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox.delete(0, tkinter.END)
        for task in tasks:
            listbox.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat.")



root=Tk()
root.title("To-Do list")

frame=Frame(root)
frame.pack()


listbox=Listbox(frame, height=15,width=50)
listbox.pack(side=LEFT)

scrollbar=Scrollbar(frame)
scrollbar.pack( side=RIGHT, fill=Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


entry_box=Entry(root, width=50)
entry_box.pack()


add_task=Button(root, text="ADD TASK", width=48, command=add_task)
add_task.pack()

delete_task=Button(root, text="DELETE TASK", width=48, command=delete_task)
delete_task.pack()

view_tasks=Button(root, text="VIEW TASKS", width=48, command=view_tasks)
view_tasks.pack()

save_tasks=Button(root, text="SAVE TASKS", width=48, command=save_tasks)
save_tasks.pack()

load_tasks=Button(root, text="LOAD TASKS", width=48, command=load_tasks)
load_tasks.pack()

root.mainloop()
