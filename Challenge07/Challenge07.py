#!/usr/bin/env python3

# Script Name:                  Python
# Author:                       Raphael Chookagian
# Date of latest revision:      06/08/2023
# Purpose:                      Create a Python script that includes the following:
          # - Assign to a variable a list of ten string elements.
          # - Print the fourth element of the list.
          # - Print the sixth through tenth element of the list.
          # - Change the value of the seventh element to "onion".

import os

# pre-check (for stretch goal)
# Delete the file if it already exists
file_path = "linux_distros_list.txt"
if os.path.isfile(file_path):
    os.remove(file_path)

# Declaration of variables

# - Assign to a variable a list of ten string elements.
linux_distros = ['Arch', 'Debian','Elementary', 'Fedora', 'Kali', 'Mint', 'Parrot','Pop', 'Ubuntu', 'Zorin']

# Main

print()
# - Print the fourth element of the list.
print("Number four on the list of Linux Distributions: ", linux_distros[3], "OS")
print()
# - Print the sixth through tenth element of the list.
print("Numbers six to ten on the list of Linux Distributions: ")
for distro in linux_distros[5:10]:
    print(distro + " OS")
print()

# - Change the value of the seventh element to "onion".
# Linux_Distros[5] = "MX"
linux_distros[6] = "onion"

print("Updated list of Linux Distributions:")
for distro in linux_distros:
    print(distro + "OS")


# Stretch goals
# I have my basic stretch goals commented out for each below. 
# The extra user prompts and things were done with the help of chatGPT

print()
# append
# Linux_Distros.append("CentOS")
user_input = input("Would you like to add a distribution? (y/n): ")
if user_input.lower() == "y":
    distro_name = input("Enter the name of the distribution you would like to add to the list: ")
    linux_distros.append(distro_name)

print()
# clear the list
# Linux_Distros.clear()
user_input = input("Would you like to clear the list? (y/n): ")
if user_input.lower() == "y":
    linux_distros.clear()
    print("List cleared.")

print()
# count occurences of element
# count_element = Linux_Distros.count("Ubuntu")
user_input = input("Would you like to count the occurrences of a distribution on this list? (y/n): ")
if user_input.lower() == "y":
    distro_name = input("Enter the name of the distribution: ")
    count_distro = linux_distros.count(distro_name)
    print(f"The distribution '{distro_name}' appears {count_distro} times in this list.")

print()
# extend/add list
# extra_distros = ["Gentoo", "Red Hat"]
# Linux_Distros.extend(extra_distros)
user_input = input("Would you like to add to the list? (y/n): ")
if user_input.lower() == "y":
    additional_distros = input("Enter the names of the distributions to add (comma-separated): ")
    distro_list = additional_distros.split(",")
    linux_distros.extend(distro_list)

print()
# index of element
# index_element = linux_distros.index("Mint")
# index of element
user_input = input("Do you want to find the index of a distribution? (y/n): ")
if user_input.lower() == "y":
    distro_name = input("Enter the name of the distribution to find the index for: ")
    try:
        index_element = linux_distros.index(distro_name)
        print(f"The distribution '{distro_name}' is found at index {index_element}.")
    except ValueError:
        print(f"The distribution '{distro_name}' was not found.")

print()
# insert at index
# linux_distros.insert(3, "Cent")
user_input = input("Would you like to insert a distribution at a specific index? (y/n): ")
if user_input.lower() == "y":
    distro_name = input("Enter the name of the distribution to insert: ")
    index = int(input("Enter the index to insert the distribution at: "))
    linux_distros.insert(index, distro_name)


print()
# - Remove an element from the list
# linux_distros.remove("Fedora")
# remove an element from the list
user_input = input("Would you like to remove a distribution from the list? (y/n): ")
if user_input.lower() == "y":
    distro_name = input("Enter the name of the distribution to remove: ")
    if distro_name in linux_distros:
        linux_distros.remove(distro_name)
        print(f"The distribution '{distro_name}' has been removed from the list.")
    else:
        print(f"The distribution '{distro_name}' is not in the list.")


# - Remove and return the last element from the list
# last_element = linux_distros.pop()
user_input = input("Would you like to remove the last element from the list? (y/n): ")
if user_input.lower() == "y":
    if len(linux_distros) > 0:
        last_element = linux_distros.pop()
        print(f"The last element '{last_element}' has been removed from the list.")
    else:
        print("The list is empty.")
else:
    print("No changes made to the list.")


print()

# - Reverse the order of the list
# linux_distros.reverse()
user_input = input("Would you like to view/display the list in reverse order? (y/n): ")
if user_input.lower() == "y":
    print("List of Linux Distributions in reverse order:")
    for distro in reversed(linux_distros):
        print(distro + "OS")
else:
    print("No changes made to the list.")



print()
# - Sort the list in ascending order
# linux_distros.sort()
# - Sort the list in ascending order
user_input = input("Would you like to view/display the list in ascending order? (y/n): ")
if user_input.lower() == "y":
    print("List of Linux Distributions in ascending order:")
    for distro in sorted(linux_distros):
        print(distro + "OS")
else:
    print("No changes made to the list.")




print()
print("Current list of Linux Distributions:")
for distro in linux_distros:
    print(distro + "OS")



print()
# copy the list
# distros_copy = linux_distros.copy()
user_input = input("Would you like to make a copy of this list? (y/n): ")
if user_input.lower() == "y":
    with open(file_path, "w") as file:
        for distro in linux_distros:
            file.write(distro + " OS\n")
    print(f"List copied to '{file_path}'.")
else:
    print("List not saved")

# End

























