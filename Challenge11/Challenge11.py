#!/usr/bin/env python3

# Script Name:                  Python
# Author:                       Raphael Chookagian
# Date of latest revision:      06/14/2023
# Purpose:                      Create a Python script that:

# * Prompt the user to type a string input as the variable for your destination URL.

# * Prompt the user to select a HTTP Method of the following options:
#   * GET
#   * POST
#   * PUT
#   * DELETE
#   * HEAD
#   * PATCH
#   * OPTIONS

# * Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.

# * Using the requests library, perform a request against the destination URL with the HTTP Method selected by the user.

# * For the given header, translate the codes into plain terms that print to the screen; for example, a 404 error should print Site not found to the terminal instead of 404.

# * For the given URL, print response header information to the screen.

import requests
import os
from datetime import datetime

# Prompt the user to type a string input as the variable for your destination URL.
print()
destination_url = input("Enter the destination URL: ")

# Add "https://" scheme if not already present
if not destination_url.startswith("http://") and not destination_url.startswith("https://"):
    destination_url = "https://" + destination_url

# Prompt the user to select an HTTP Method
http_methods = [
    "GET",
    "POST",
    "PUT",
    "DELETE",
    "HEAD",
    "PATCH"
]

# Dictionary mapping status codes to plain terms
status_codes = {
    200: "OK",
    201: "Created",
    204: "No Content",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    500: "Internal Server Error"
}

# Variable to store the current file name
current_file = ""

while True:
    # Display the main menu
    print("\nMain Menu:")
    print()
    for i, method in enumerate(http_methods):
        print(f"{i + 1}. {method}")
    print(f"{len(http_methods) + 1}. OPTIONS")
    print(f"{len(http_methods) + 2}. QUIT")

    # Get user input for the main menu
    print()
    user_input = input("Enter the number of the desired option: ")

    if user_input == str(len(http_methods) + 1):
        # Display the options menu
        while True:
            print("\nOptions Menu:")
            print("1. Save requests and responses to a file")
            print("2. Open saved file")
            print("3. Update saved file")
            print("4. Delete saved file")
            print("5. Back to Main Menu")

            # Get user input for the options menu
            options_input = input("Enter the number of the desired option: ")

            if options_input == "1":
                if current_file == "":
                    print("No current file. Please select a file to save.")
                else:
                    # Save requests and responses to the current file
                    with open(current_file, "a") as file:
                        file.write(f"\nURL: {destination_url}\n")
                        file.write(f"Method: OPTIONS\n")
                    print()    
                    print("Requests and responses saved to the current file.")
            elif options_input == "2":
                # Open saved file
                file_list = os.listdir()
                if not file_list:
                    print("No files found.")
                else:
                    print("Available files:")
                    for i, file_name in enumerate(file_list):
                        print(f"{i + 1}. {file_name}")
                    file_number = input("Enter the number of the file to open: ")
                    try:
                        selected_file = file_list[int(file_number) - 1]
                        with open(selected_file, "r") as file:
                            content = file.read()
                            print(content)
                        # Set the current file to the opened file
                        current_file = selected_file
                    except (ValueError, IndexError):
                        print("Invalid file number.")
            elif options_input == "3":
                # Update saved file
                if current_file == "":
                    print("No current file. Please select a file to update.")
                else:
                    file_list = os.listdir()
                    if not file_list:
                        print("No files found.")
                    else:
                        print("Available files:")
                        for i, file_name in enumerate(file_list):
                            print(f"{i + 1}. {file_name}")
                        file_number = input("Enter the number of the file to update: ")
                        try:
                            selected_file = file_list[int(file_number) - 1]
                            if selected_file == current_file:
                                print("Cannot update the current file.")
                            else:
                                with open(selected_file, "w") as file:
                                    file.write(f"URL: {destination_url}\n")
                                    file.write(f"Method: OPTIONS\n")
                                print(f"File '{selected_file}' updated.")
                        except (ValueError, IndexError):
                            print("Invalid file number.")
            elif options_input == "4":
                # Delete saved file
                file_list = os.listdir()
                if not file_list:
                    print("No files found.")
                else:
                    print("Available files:")
                    for i, file_name in enumerate(file_list):
                        print(f"{i + 1}. {file_name}")
                    file_number = input("Enter the number of the file to delete: ")
                    try:
                        selected_file = file_list[int(file_number) - 1]
                        if selected_file == current_file:
                            print("Cannot delete the current file.")
                        else:
                            os.remove(selected_file)
                            print(f"File '{selected_file}' deleted.")
                    except (ValueError, IndexError):
                        print("Invalid file number.")
            elif options_input == "5":
                # Go back to the main menu
                break
            else:
                print("Invalid option.")
    elif user_input == str(len(http_methods) + 2):
        # Quit the program
        print("Quitting...")
        break
    elif user_input.isdigit() and 1 <= int(user_input) <= len(http_methods):
        # Valid HTTP method selected
        http_method = http_methods[int(user_input) - 1]

        # Print the entire request
        print("\nRequest:")
        print()
        print(f"URL: {destination_url}")
        print()
        print(f"Method: {http_method}")
        print()

        # Ask for confirmation before proceeding
        while True:
            confirm = input("Confirm the request (yes/no): ").lower()
            if confirm == "yes":
                try:
                    # Set a timeout for the request (in seconds)
                    timeout = 5

                    # Perform the request using the requests library with timeout
                    response = requests.request(http_method, destination_url, timeout=timeout)

                    # Print response header information
                    print("\nResponse Header:")
                    for key, value in response.headers.items():
                        print(f"{key}: {value}")

                    # Print response body
                    print("\nResponse Body:")
                    print(response.text)
                    print()

                    # Translate status code into plain term
                    status_code = response.status_code
                    if status_code in status_codes:
                        status_term = status_codes[status_code]
                        print(f"\nStatus: {status_code} - {status_term}")
                    else:
                        print(f"\nStatus: {status_code}")

                    # Save requests and responses to a file
                    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                    filename = f"http_output_{current_datetime}.txt"
                    with open(filename, "w") as file:
                        file.write(f"URL: {destination_url}\n")
                        file.write(f"Method: {http_method}\n")
                        file.write(f"Response Header:\n")
                        for key, value in response.headers.items():
                            file.write(f"{key}: {value}\n")
                        file.write(f"\nResponse Body:\n{response.text}\n")
                    print(f"Requests and responses saved to the file: {filename}")
                    # Set the current file to the saved file
                    current_file = filename
                    break
                except requests.exceptions.RequestException as e:
                    print(f"An error occurred during the request: {e}")
                    break
            elif confirm == "no":
                print("Request canceled.")
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
    else:
        print("Invalid option.")





# End
