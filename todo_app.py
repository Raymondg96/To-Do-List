#import modules
from tkinter import *
from tkinter import ttk
from tkinter import font



# #display a menu
# def display_menu():
#     print("Menu")
#     print("1. Add Task")
#     print("2. View Tasks")
#     print("3. Mark as Done")
#     print("4. Exit")

# #add tasks
# def add_task(tasks):
#     task=input("Enter task: ")
#     tasks.append(task)
#     print("Task added successfully!")

# #view tasks
# def view_tasks(tasks):
#     print("\nTasks:")
#     for i, task in enumerate(tasks, start=1):
#         print(f"{i}. {task}")

# #mark tasks done
# def mark_task_done(tasks):
#     if not tasks:
#         print("No tasks to mark as done.")
#         return
    
#     view_tasks(tasks) #display tasks with indices
#     index=int(input("Enter task index to mark as done: "))-1

#     if 0<=index<len(tasks):
#         removed_task=tasks.pop(index)
#         print(f"Task '{removed_task}' marked as done and removed.")
#     else:
#         print("Invalid task index.")

# def save_tasks(tasks):
#     with open("tasks.txt", "w") as f:
#         for task in tasks:
#             f.write(task + '\n')


# def load_tasks():
#     try:
#         with open("tasks.txt", "r") as f:
#             return f.read().splitlines()
#     except FileNotFoundError:
#         return []

# #main program logic
# def main():
#     tasks = load_tasks()  # Load tasks from file

#     while True:
#         display_menu()

#         choice=input("Enter your choice:")
#         if choice == '1':
#             add_task(tasks)
#         elif choice == '2':
#             view_tasks(tasks)
#         elif choice == '3':
#             mark_task_done(tasks)
#         elif choice == '4':
#             print("Exiting.")
#             save_tasks(tasks)
#             break
#         else:
#             print("Invalid choice. Please select a valid option.")


#initialize window
root = Tk()
root.title("Ray's To Do")
root.geometry("500x500")

#create frame
my_frame = Frame(root)
my_frame.pack(pady=10)

#create listbox
my_list = Listbox(my_frame,width=25,height=5,bg="SystemButtonFace",bd=0,fg="#464646")
my_list.pack()

#create dummy list
stuff = ["learn tkinter", "module 4", "module 5"]
#add dummy list to list box
for item in stuff:
    my_list.insert(END, item)

root.mainloop()