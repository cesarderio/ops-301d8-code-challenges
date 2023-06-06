#!/usr/bin/env python3

# Script Name:                  Bash in Python
# Author:                       Raphael Chookagian
# Date of latest revision:      06/06/2023
# Purpose:                      Create a Python script that executes a few bash commands successfully. Indicate in comments how you achieved this.


# import "OS" or "subprocess" comment out the one you do not want to use.
import os
# import subprocess

# Declare Functions
# function to execute command
def Xacute(command):
    stream = os.popen(command)
    output = stream.read()
    return output.strip()

# Declare Variables
# variables for commands whoami, ip and lshw
whoami = Xacute('whoami')

ip = Xacute('ip a')

lshw = Xacute('lshw -short')


# Main

# Commands and description of commands
print("Output of 'whoami':")
print(whoami)

print("\nOutput of 'ip a':")
print(ip)

print("\nOutput of 'lshw -short':")
print(lshw)

# End
