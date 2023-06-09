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
print()
# - Print the fourth element of the list.
print("Number four on the list of Linux Distributions:", Linux_Distros[3], "OS")
print()
# - Print the sixth through tenth element of the list.
print("Numbers six to ten on the list of Linux Distributions:")
for distro in Linux_Distros[5:10]:
    print(distro + "OS")

# - Change the value of the seventh element to "onion".
# Linux_Distros[5] = "MX"
Linux_Distros[6] = "onion"

# print("Updated list of Linux Distributions:", Linux_Distros)



# Stretch goals

# append
Linux_Distros.append("CentOS")

# clear the list
# Linux_Distros.clear()

# copy the list
distros_copy = Linux_Distros.copy()

# count occurences of element
count_element = Linux_Distros.count("Ubuntu")

# extend/add list
# extra_distros = ["Gentoo", "Red Hat"]
# Linux_Distros.extend(extra_distros)

# index of element
index_element = Linux_Distros.index("Mint")

# insert at index
Linux_Distros.insert(3, "Cent")

# - Remove an element from the list
Linux_Distros.remove("Fedora")

# - Remove and return the last element from the list
last_element = Linux_Distros.pop()

# - Reverse the order of the list
Linux_Distros.reverse()

# - Sort the list in ascending order
Linux_Distros.sort()

print()
print("Updated list of Linux Distributions:", Linux_Distros)

# End
