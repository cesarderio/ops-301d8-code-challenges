#!/usr/bin/env python3

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
            print("List has been cleared.")
        elif command == "copy":
            file_path = "Linux_List.txt"
            with open(file_path, "w") as file:
                for distro in linux_distros:
                    file.write(distro + " OS\n")
            print(f"List copied to '{file_path}'.")
        elif command == "count":
            distro_name = input("Enter the name of the distribution: ")
            count_distro = linux_distros.count(distro_name)
            print(f"The distribution '{distro_name}' appears {count_distro} times in this list.")
        elif command == "extend":
            additional_distros = input("Enter the names of the distributions to add (comma-separated): ")
            distro_list = additional_distros.split(",")
            linux_distros.extend(distro_list)
        elif command == "index":
            distro_name = input("Enter the name of the distribution to find the index for: ")
            try:
                index_element = linux_distros.index(distro_name)
                print(f"The distribution '{distro_name}' is found at index {index_element}.")
            except ValueError:
                print(f"The distribution '{distro_name}' was not found.")
        elif command == "insert":
            distro_name = input("Enter the name of the distribution to insert: ")
            index = int(input("Enter the index to insert the distribution at: "))
            linux_distros.insert(index, distro_name)
        elif command == "last":
            last_element = linux_distros[-1]
            print(f"The last element of the list is '{last_element}'.")
        elif command == "remove":
            distro_name = input("Enter the name of the distribution to remove: ")
            if distro_name in linux_distros:
                linux_distros.remove(distro_name)
                print(f"The distribution '{distro_name}' has been removed from the list.")
            else:
                print(f"The distribution '{distro_name}' is not in the list.")
        elif command == "reverse":
            linux_distros.reverse()
            print("The list has been reversed.")
