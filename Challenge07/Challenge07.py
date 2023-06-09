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

# print("Updated list of Linux Distributions:")
# for distro in linux_distros:
#     print(distro + "OS")

# # Stretch goals
# # I have my basic stretch goals commented out or over on the Tester.py file. 
# # The extra user prompts and things were done with the help of chatGPT



# Tuple
yo_tuple = (1, 2, 3, 4, 5)

# Set
yo_set = {1, 2, 3, 4, 5}

# Dictionary
yo_dicto = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# # append
# # Linux_Distros.append("CentOS")

# # clear the list
# # Linux_Distros.clear()

# count occurences of element
# count_element = Linux_Distros.count("Ubuntu")

# extend/add list
# extra_distros = ["Gentoo", "Red Hat"]
# Linux_Distros.extend(extra_distros)

# index of element
# index_element = linux_distros.index("Mint")

# insert at index
# linux_distros.insert(3, "Cent")

# remove an element from the list
# linux_distros.remove("Fedora")

# - Remove and return the last element from the list
# last_element = linux_distros.pop()

# - Reverse the order of the list
# linux_distros.reverse()

# # - Sort the list in ascending order
# # linux_distros.sort()

# print("Current list of Linux Distributions:")
# for distro in linux_distros:
#     print(distro + "OS")

# # copy the list
# # distros_copy = linux_distros.copy()
print()

def main_menu():
    print()
    print("Select a command:")
    print()
    for i, command in enumerate(commands):
        print(f"{i + 1}. {command}")

print("List of Linux Distributions:")
for distro in linux_distros:
    print(distro + " OS")

commands = [
    "append",
    "ascending",
    "clear",
    "copy",
    "count",
    "extend",
    "index",
    "insert",
    "last",
    "remove",
    "reverse",
    "delete file"
]

commands.sort()  # Sort the commands in alphabetical order

while True:
    main_menu()
    print()
    user_input = input("Enter the number of the command you want to execute (or 'q' to quit): ")
    if user_input.lower() == "q":
        break
    command_index = int(user_input) - 1

    if command_index >= 0 and command_index < len(commands):
        command = commands[command_index]
        if command == "append":
            print()
            distro_name = input("Enter the name of the distribution you would like to add to the list: ")
            linux_distros.append(distro_name)
            print()
            print("Updated list of Linux Distributions:")
            print()
            for distro in linux_distros:
                print(distro + " OS")
        elif command == "ascending":
            linux_distros.sort()
            print()
            print("Linux Distributions sorted in ascending order:")
            print()
            for distro in linux_distros:
                print(distro + " OS")
        elif command == "clear":
            linux_distros.clear()
            print()
            print("List has been cleared.")
        elif command == "copy":
            file_path = "Linux_List.txt"
            with open(file_path, "w") as file:
                for distro in linux_distros:
                    file.write(distro + " OS\n")
            print()
            print(f"List copied to '{file_path}'.")
        elif command == "count":
            print()
            distro_name = input("Enter the name of the distribution: ")
            count_distro = linux_distros.count(distro_name)
            print()
            print(f"The distribution '{distro_name}' appears {count_distro} times in this list.")
        elif command == "extend":
            print()
            additional_distros = input("Enter the names of the distributions to add (comma-separated): ")
            distro_list = additional_distros.split(",")
            linux_distros.extend(distro_list)
            print()
            print("Updated list of Linux Distributions:")
            print()
            for distro in linux_distros:
                print(distro + " OS")
        elif command == "index":
            print()
            distro_name = input("Enter the name of the distribution to find the index for: ")
            try:
                index_element = linux_distros.index(distro_name)
                print()
                print(f"The distribution '{distro_name}' is found at index {index_element}.")
            except ValueError:
                print(f"The distribution '{distro_name}' was not found.")
        elif command == "insert":
            distro_name = input("Enter the name of the distribution to insert: ")
            index = int(input("Enter the index to insert the distribution at: "))
            linux_distros.insert(index, distro_name)
            print()
            print("Updated list of Linux Distributions:")
            print()
            for distro in linux_distros:
                print(distro + " OS")
        elif command == "last":
            last_element = linux_distros[-1]
            print()
            print(f"The last element of the list is '{last_element}'.")
        elif command == "remove":
            print()
            distro_name = input("Enter the name of the distribution to remove: ")
            if distro_name in linux_distros:
                linux_distros.remove(distro_name)
                print()
                print(f"The distribution '{distro_name}' has been removed from the list.")
                print()
                for distro in linux_distros:
                  print(distro + " OS")
            else:
                print()
                print(f"The distribution '{distro_name}' is not in the list.")
        elif command == "reverse":
            linux_distros.reverse()
            print()
            print("The list of Linux distributions in reverse order:")
            print()
            for distro in linux_distros:
                print(distro + " OS")
        elif command == "delete file":
            file_path = "Linux_List.txt"
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"File '{file_path}' has been deleted.")
            else:
                print(f"File '{file_path}' does not exist.")




# End
