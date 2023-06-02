#!/bin/bash

# Script Name:                  Copy & Append Date and Time
# Author:                       Raphael Chookagian
# Date of latest revision:      06/02/2023
# Purpose:                      Create a bash script that launches a menu system with the following options:

  # Hello world (prints “Hello world!” to the screen)

  # Ping self (pings this computer’s loopback address)

  # IP info (print the network adapter information for this computer)

  # Exit

# Next, the user input should be requested.

# The program should next use a conditional statement to evaluate the user’s input, then act according to what the user selected.

# Use a loop to bring up the menu again after the request has been executed.








# Main

# Check for correct IP info command
if command -v ip &> /dev/null; then
    IPinfo="ip addr show"
else
    if command -v ifconfig &> /dev/null; then
        IPinfo="ifconfig"
    else
        echo "Error: unknown command"
        exit 1
    fi
fi

while true; do
    # options
    echo "Menu:"
    echo "1. Hello world"
    echo "2. Ping self"
    echo "3. IP info"
    echo "4. Exit"
    
    # user input
    read -p "Please input a selection number and hit enter: " choice
    case $choice in
        1)
            echo
            echo "Hello world!"
            ;;
        2)
            ping -c 4 127.0.0.1
            ;;
        3)
            $IPinfo
            ;;
        4)
            echo "Have a nice day!"
            exit 0
            ;;
        *)
            echo "Invalid, try again"
            ;;
    esac
    
    echo
    # back to main menu or exit
    read -p "Please type 'exit' to quit or press enter to continue to main menu: " continue_choice
    if [[ $continue_choice == "exit" ]]; then
        echo "Have a nice day!"
        exit 0
    fi
done

# Fin
