#Importing the modules
import argparse  #For CL argument parsing
import os        #For OS operations

"""Here we have to set up the argument Parser
We gonna be using CL flags to add, list and remove tasks. 
let's manage to use both short and long options for each argument
  '-a' or '--add' to add tasks
  '-l' or '--list' to list all tasks
  '-r' or '--remove' to remove tasks using index   

By leveraging argparse module to parse the arguments provided at the command line
"""

#Adding arguments to Create_parser() function plus their corresponding help message
def create_parser():
    parser =argparse.ArgumentParser(description="CLI TOdo List App")
    parser.add_argument("-a","--add", metavar="", help="Add a new task")
    parser.add_argument("-l", "--list", metavar="", help="List all the tasks")
    parser.add_argument("-r", "--remove", metavar="", help="Remove a task by index")
    return parser
