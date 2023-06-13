#!/usr/bin/env python3

# Script Name:                  Python
# Author:                       Raphael Chookagian
# Date of latest revision:      06/12/2023
# Purpose:                      Create a Python script that:

# Using file handling commands, create a Python script that creates a new .txt file, appends three lines, prints to the screen the first line, then deletes the .txt file.

import os

# Declaration of variables

# Open file in write mode to create new file
file_name = "Code_Challenge_class10.txt"
file = open(file_name, "w")

# Main

# Add/Append three lines to file
file.write("Welcome\n")
file.write("to the\n")
file.write("Danger Zone!\n")

# Close file
file.close()

# Open the file in read mode
file = open(file_name, "r")

# Read the first line and print it
# first_line = file.readline()
# print("First line:", first_line)
lines = file.readlines()
print("First line:", lines[0])
print("Second line:", lines[1])
print("Third line:", lines[2])

# Close file
file.close()

# Delete file
os.remove(file_name)

# End
