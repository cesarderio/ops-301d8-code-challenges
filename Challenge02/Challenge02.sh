#!/bin/bash

# Script Name:                  Copy & Append Date and Time
# Author:                       Raphael Chookagian
# Date of latest revision:      05/31/2023
# Purpose:                      Create a bash script that:

# Prompts user for input directory path.
# Prompts user for input permissions number (e.g. **777** to perform a **chmod 777**)
# Navigates to the directory input by the user and changes all files inside it to the input setting.
# Prints to the screen the directory contents and the new permissions settings of everything in the directory.

# Main


# Check if script is running with root privileges
if [[ $EUID -ne 0 ]]; then
    # Add sudo
    sudo bash "$0"
    exit 0
fi


# Prompts user for input directory path.
read -p "Enter your target directory path: " directory

# Check if directory exists
if [ -d "$directory" ]; then
    
# Prompts user for input permissions number (e.g. **777** to perform a **chmod 777**)
    read -p "Enter permissions number (e.g. 777): " permissions
    
    # Check for valid input
    if [[ $permissions =~ ^[0-7]{3}$ ]]; then

# Navigates to the directory input by the user and changes all files inside it to the input setting.
        for file in "$directory"/*; do
            if [ -f "$file" ]; then
                # execute chmod command
                chmod "$permissions" "$file"
                echo "Permissions updated: $file"
            fi
        done
        
# Prints to the screen the directory contents and the new permissions settings of everything in the directory.
        echo "Updated directory settings:"
        ls -l "$directory"
    else
        echo "Invalid input, Enter a valid 3-digit number."
    fi
else
    echo "'$directory' does not exist."
fi

# End
