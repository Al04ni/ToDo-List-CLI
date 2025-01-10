#Importing the modules
import argparse  #For CL argument parsing
import os        #For OS operations

"""Here we have to set up the argument Parser
   We gonna be using CL flags to add, list and remove tasks. 
   let's manage to use both short and long options for each argument
   + '-a' or '--add' to add tasks
   +'-l' or '--list' to list all tasks
   +'-r' or '--remove' to remove tasks using index   

   By leveraging argparse module to parse the arguments provided at the command line
"""

#Adding arguments to Create_parser() function plus their corresponding help message
def create_parser():
    parser = argparse.ArgumentParser(description="CLI TOdo List App")
    parser.add_argument("-a","--add", metavar="", help="Add a new task")
    parser.add_argument("-l", "--list", metavar="", help="List all the tasks")
    parser.add_argument("-r", "--remove", metavar="", help="Remove a task by index")
    return parser


#Adding task management functions
    """we gonna define functions to perform the task based on the above arguments
    to perform operations:
    + Adding a task
    + Listing all tasks
    + Removing task by its index
    Let's keep hacking *_*
    """

def add_task(task): 
    #To interact with simple text file in 'append mode' to add tasks
    with open("tasks.txt", "a") as file:
        file.write(task +"\n")
    #Using 'with' statement to manage file
    
def list_tasks(task):
    #For listing all the tasks and check file existence
    #Firstly we have to check for the file
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for index, task in enumerate(tasks, start=1):
                print(f"{index}.{task.strip}")
                
    else:
        print("No tasks found.")
        
def remove_task(index):
    #After also checking the file existence, we open file in
    #write mode to overwrites the existing file
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        with open("tasks.txt","w") as file:
            for i, task in enumerate(tasks, start=1):
                if i != index:
                    file.write(task)
                    print("Task removed successfully")
                    
                else:
                    print("No task found")
                    
                    
