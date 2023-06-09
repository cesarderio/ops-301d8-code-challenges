#!/usr/bin/env python3




# print()
# # append
# # Linux_Distros.append("CentOS")
# user_input = input("Would you like to add a distribution? (y/n): ")
# if user_input.lower() == "y":
#     distro_name = input("Enter the name of the distribution you would like to add to the list: ")
#     linux_distros.append(distro_name)

# print()
# # clear the list
# # Linux_Distros.clear()
# user_input = input("Would you like to clear the list? (y/n): ")
# if user_input.lower() == "y":
#     linux_distros.clear()
#     print("List cleared.")

# print()
# # count occurences of element
# # count_element = Linux_Distros.count("Ubuntu")
# user_input = input("Would you like to count the occurrences of a distribution on this list? (y/n): ")
# if user_input.lower() == "y":
#     distro_name = input("Enter the name of the distribution: ")
#     count_distro = linux_distros.count(distro_name)
#     print(f"The distribution '{distro_name}' appears {count_distro} times in this list.")

# print()
# # extend/add list
# # extra_distros = ["Gentoo", "Red Hat"]
# # Linux_Distros.extend(extra_distros)
# user_input = input("Would you like to add to the list? (y/n): ")
# if user_input.lower() == "y":
#     additional_distros = input("Enter the names of the distributions to add (comma-separated): ")
#     distro_list = additional_distros.split(",")
#     linux_distros.extend(distro_list)

# print()
# # index of element
# # index_element = linux_distros.index("Mint")
# # index of element
# user_input = input("Do you want to find the index of a distribution? (y/n): ")
# if user_input.lower() == "y":
#     distro_name = input("Enter the name of the distribution to find the index for: ")
#     try:
#         index_element = linux_distros.index(distro_name)
#         print(f"The distribution '{distro_name}' is found at index {index_element}.")
#     except ValueError:
#         print(f"The distribution '{distro_name}' was not found.")

# print()
# # insert at index
# # linux_distros.insert(3, "Cent")
# user_input = input("Would you like to insert a distribution at a specific index? (y/n): ")
# if user_input.lower() == "y":
#     distro_name = input("Enter the name of the distribution to insert: ")
#     index = int(input("Enter the index to insert the distribution at: "))
#     linux_distros.insert(index, distro_name)

# print()
# # - Remove an element from the list
# # linux_distros.remove("Fedora")
# # remove an element from the list
# user_input = input("Would you like to remove a distribution from the list? (y/n): ")
# if user_input.lower() == "y":
#     distro_name = input("Enter the name of the distribution to remove: ")
#     if distro_name in linux_distros:
#         linux_distros.remove(distro_name)
#         print(f"The distribution '{distro_name}' has been removed from the list.")
#     else:
#         print(f"The distribution '{distro_name}' is not in the list.")

# # - Remove and return the last element from the list
# # last_element = linux_distros.pop()
# user_input = input("Would you like to remove the last element from the list? (y/n): ")
# if user_input.lower() == "y":
#     if len(linux_distros) > 0:
#         last_element = linux_distros.pop()
#         print(f"The last element '{last_element}' has been removed from the list.")
#     else:
#         print("The list is empty.")
# else:
#     print("No changes made to the list.")

# print()

# # - Reverse the order of the list
# # linux_distros.reverse()
# user_input = input("Would you like to view/display the list in reverse order? (y/n): ")
# if user_input.lower() == "y":
#     print("List of Linux Distributions in reverse order:")
#     for distro in reversed(linux_distros):
#         print(distro + "OS")
# else:
#     print("No changes made to the list.")

# print()
# # - Sort the list in ascending order
# # linux_distros.sort()
# # - Sort the list in ascending order
# user_input = input("Would you like to view/display the list in ascending order? (y/n): ")
# if user_input.lower() == "y":
#     print("List of Linux Distributions in ascending order:")
#     for distro in sorted(linux_distros):
#         print(distro + "OS")
# else:
#     print("No changes made to the list.")

# print()
# print("Current list of Linux Distributions:")
# for distro in linux_distros:
#     print(distro + "OS")

# print()
# # copy the list
# # distros_copy = linux_distros.copy()
# user_input = input("Would you like to make a copy of this list? (y/n): ")
# if user_input.lower() == "y":
#     with open(file_path, "w") as file:
#         for distro in linux_distros:
#             file.write(distro + " OS\n")
#     print(f"List copied to '{file_path}'.")
# else:
#     print("List not saved")




def main_menu():
    print()
    print("Select a command:")
    print()
    for i, command in enumerate(commands):
        print(f"{i + 1}. {command}")

linux_distros = ['Arch', 'Debian', 'Elementary', 'Fedora', 'Kali', 'Mint', 'Parrot', 'Pop', 'Ubuntu', 'Zorin']

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
