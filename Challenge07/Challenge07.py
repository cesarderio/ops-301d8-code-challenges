#!/usr/bin/env python3

# Script Name:                  Bash in Python
# Author:                       Raphael Chookagian
# Date of latest revision:      06/07/2023
# Purpose:                      Create a Python script that includes the following:
          # - Assign to a variable a list of ten string elements.
          # - Print the fourth element of the list.
          # - Print the sixth through tenth element of the list.
          # - Change the value of the seventh element to "onion".

# Declaration of variables
# - Assign to a variable a list of ten string elements.
Linux_Distros = ['Arch', 'Debian','Elementary', 'Fedora', 'Kali', 'Mint', 'Parrot','Pop', 'Ubuntu', 'Zorin']

# Main
# - Print the fourth element of the list.
print("Number four on the list of Linux Distributions:", Linux_Distros[3], "OS")

# - Print the sixth through tenth element of the list.
print("Numbers six to ten on the list of Linux Distributions:")
for distro in Linux_Distros[5:10]:
    print(distro + "OS")

# - Change the value of the seventh element to "onion".
# Linux_Distros[5] = "MX"
Linux_Distros[6] = "onion"

print("Updated list of Linux Distributions:", Linux_Distros)

# End
