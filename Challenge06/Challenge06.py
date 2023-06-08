#!/usr/bin/env python3

# Script Name:                  Bash in Python
# Author:                       Raphael Chookagian
# Date of latest revision:      06/07/2023
# Purpose:                      Create a Python script that generates all directories, sub-directories and files for a user-provided directory path.

# - Script must ask the user for a file path and read a user input string into a variable.
# - Script must use the `os.walk()` function from the `os` library.
# - Script must enclose the `os.walk()` function within a python function that hands it the user input file path.



# Import libraries

import os

# Declaration of variables

# Ask the user for a directory/file path
user_input = input("Enter a directory path: ")


# Declaration of functions

def gen_dir_tree(directory_path):
  for root, dirs, files in os.walk(directory_path):
    print("Root Directory:", root)
    print("Directories:")
    for directory in dirs:
      print(os.path.join(root, directory))
      print("Files:")
      for file in files:
          print(os.path.join(root, file))


# Main

# Call function
gen_dir_tree(user_input)

# End
