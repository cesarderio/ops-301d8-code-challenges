import requests

# Prompt the user to enter their personal access token
personal_access_token = input("Enter your personal access token: ")

# Set the headers with the authentication token
headers = {
    "Authorization": f"Bearer {personal_access_token}"
}

# Prompt the user to type a string input as the variable for your destination URL.
destination_url = input("Enter the destination URL: ")

# Prompt the user to select an HTTP Method
http_methods = [
    "GET",
    "POST",
    "PUT",
    "DELETE",
    "HEAD",
    "PATCH",
    "OPTIONS"
]
print("Select an HTTP Method:")
for i, method in enumerate(http_methods):
    print(f"{i + 1}. {method}")
print(f"{len(http_methods) + 1}. Save requests and responses to a file")
print(f"{len(http_methods) + 2}. Open saved file")
print(f"{len(http_methods) + 3}. Update saved file")
print(f"{len(http_methods) + 4}. Delete saved file")

# Get user input for HTTP Method
while True:
    try:
        method_index = int(input("Enter the number of the desired HTTP Method: ")) - 1
        if method_index == len(http_methods):
            # Save requests and responses to a file
            filename = input("Enter the filename to save requests and responses: ")
            with open(filename, "w") as file:
                file.write(f"URL: {destination_url}\n")
                file.write(f"Method: {http_method}\n")
                file.write("Request Headers:\n")
                for header, value in headers.items():
                    file.write(f"{header}: {value}\n")
                file.write("\n")
                file.write("Response Headers:\n")
                for header, value in response.headers.items():
                    file.write(f"{header}: {value}\n")
                file.write("\n")
                file.write("Response Body:\n")
                file.write(response.text)
            print("Requests and responses saved to the file.")
            exit()
        elif method_index == len(http_methods) + 1:
            # Open saved file
            filename = input("Enter the filename to open: ")
            try:
                with open(filename, "r") as file:
                    content = file.read()
                    print(content)
            except FileNotFoundError:
                print("File not found.")
            exit()
        elif method_index == len(http_methods) + 2:
            # Update saved file
            filename = input("Enter the filename to update: ")
            try:
                with open(filename, "a") as file:
                    file.write("\n")
                    file.write(f"URL: {destination_url}\n")
                    file.write(f"Method: {http_method}\n")
                    file.write("Request Headers:\n")
                    for header, value in headers.items():
                        file.write(f"{header}: {value}\n")
                    file.write("\n")
                    file.write("Response Headers:\n")
                    for header, value in response.headers.items():
                        file.write(f"{header}: {value}\n")
                    file.write("\n")
                    file.write("Response Body:\n")
                    file.write(response.text)
                print("File updated successfully.")
            except FileNotFoundError:
                print("File not found.")
            exit()
        elif method_index == len(http_methods) + 3:
            # Delete saved file
            filename = input("Enter the filename to delete: ")
            try:
                os.remove(filename)
                print("File deleted successfully.")
            except FileNotFoundError:
                print("File not found.")
            exit()
        http_method = http_methods[method_index]
        break
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid number.")

# Print the entire request
print("Request:")
print(f"URL: {destination_url}")
print(f"Method: {http_method}")

# Ask for confirmation before proceeding
while True:
    confirm = input("Confirm the request (yes/no): ").lower()
    if confirm == "yes":
        break
    elif confirm == "no":
        print("Request cancelled.")
        exit()
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

try:
    # Set a timeout for the request (in seconds)
    timeout = 5

    # Perform the request using the requests library with authentication and timeout
    response = requests.request(http_method, destination_url, headers=headers, timeout=timeout)

    # Print response header information
    print("\nResponse Headers:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")
    print("\nResponse Body:")
    print(response.text)
except requests.RequestException as e:
    print(f"An error occurred during the request: {e}")
