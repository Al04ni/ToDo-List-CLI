"""Importing all necessary modules"""
import argparse  #For CL argument parsing
import os        #For OS operations

#Here we have to set up the argument Parser
"""We gonna be using CL flags to add, list and remove tasks. 
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

# Configuration
TASKS_FILE = "tasks.txt"  # Can be modified or loaded from environment/config

def add_task(task): 
    try:
        with open(TASKS_FILE, "a") as file:
            file.write(task + "\n")
    except IOError as e:
        print(f"Error adding task: {e}")
        raise

def list_tasks(task):
    try:
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r") as file:
                tasks = file.readlines()
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}.{task.strip()}")
        else:
            print(f"Tasks file {TASKS_FILE} does not exist")
    except IOError as e:
        print(f"Error reading tasks: {e}")
        raise
        
def remove_task(index):
    """Removes a task by its index after validating the index and file existence."""

    try:
        index = int(index)  # Convert index to integer and validate
    except ValueError:
        print("Invalid index. Please provide an integer.")
        return

    if not os.path.exists("tasks.txt"):
        print("No tasks found.")
        return

    with open("tasks.txt", "r") as file:
        tasks = file.readlines()

    if 1 <= index <= len(tasks):  # Check if the index is within the valid range
        with open("tasks.txt", "w") as file:
            for i, task in enumerate(tasks, start=1):
                if i != index:
                    file.write(task)
        print(f"Task {index} removed successfully.") # Success message after removal
    else:
        print(f"Task {index} not found.") # Failure message if task not found


#Setting the parser tp parse CL arguments by calling them ASAP
def main():
    parser = create_parser()
    args = parser.parse_args()
    
    if args.add:
        add_task(args.add)
    elif args.list:
        list_tasks()
    elif args.remove():
        remove_task(int(args.remove))
    
    else:
        parser.print_help()
        
if __name__ == "__main__":
    main()
