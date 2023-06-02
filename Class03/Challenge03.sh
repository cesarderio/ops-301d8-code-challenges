#!/bin/bash

# Script Name:                  Copy & Append Date and Time
# Author:                       Raphael Chookagian
# Date of latest revision:      06/02/2023
# Purpose:                      Create a bash script that launches a menu system with the following options:

  # * Hello world (prints “Hello world!” to the screen)

  # * Ping self (pings this computer’s loopback address)

  # * IP info (print the network adapter information for this computer)

  # * Exit

# Main

#!/bin/bash

while true; do
    # options
    echo "Menu:"
    echo "1. Hello world"
    echo "2. Ping self"
    echo "3. IP info"
    echo "4. Exit"
    
    # Prompt for user input
    read -p "Please input a selection number and hit enter: " choice
    
    case $choice in
        1)
            # Hello world
            echo "Hello world!"
            ;;
        2)
            # Ping self
            ping -c 4 127.0.0.1
            ;;
        3)
            # Option: IP info
            ifconfig
            ;;
        4)
            # Exit
            echo "Have a nice day!"
            exit 0
            ;;
        *)
            echo "Invalid, try again"
            ;;
    esac
    
    echo
    # Prompt to continue or exit
    read -p "Please type 'exit' to quit or press enter to continue to main menu: " continue_choice
    
    if [[ $continue_choice == "exit" ]]; then
        echo "Have a nice day!"
        exit 0
    fi
    
    echo # Empty line for readability
done
