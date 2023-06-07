#!/usr/bin/env python3

# Script Name:                  Bash in Python
# Author:                       Raphael Chookagian
# Date of latest revision:      06/06/2023
# Purpose:                      Create a Python script that executes a few bash commands successfully. Indicate in comments how you achieved this.


# import "OS" or "subprocess" comment out the one you do not want to use.
import os
# import subprocess

# function to execute command
def Xacute(command):
    stream = os.popen(command)
    output = stream.read()
    return output.strip()



# home directory of current user
home_dir = os.path.expanduser('~')
output_file = os.path.join(home_dir, 'Desktop', 'PyBash_output.txt')

# Check file exists
if not os.path.exists(output_file):
    open(output_file, 'w').close()

with open(output_file, 'a') as file:

    # Variable for command
    whoami = Xacute('whoami')
    # Command and description of command
    print("Output of 'whoami':")
    print(whoami)
    # Save output to file on desktop
    file.write("Output of 'whoami':\n")
    file.write("\n\n")
    file.write(whoami)

    # Variable for command
    ip = Xacute('ip a')
    # Commands and description of commands
    print("\nOutput of 'ip a':")
    print(ip)
    # Save output to file on desktop
    file.write("Output of 'ip a':\n")
    file.write(ip)
    file.write("\n\n")

    # Variable for command
    lshw = Xacute('lshw -short')
    # Commands and description of commands
    print("\nOutput of 'lshw -short':")
    print(lshw)
    # Save output to file on desktop
    file.write("Output of 'lshw -short':\n")
    file.write(lshw)
    file.write("\n\n")

# End
