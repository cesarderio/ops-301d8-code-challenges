import tkinter as tk
from tkinter import messagebox

class PasswordKeeperGUI:
    def __init__(self, password_keeper):
        self.password_keeper = password_keeper

        # Create the main window
        self.root = tk.Tk()
        self.root.title("Password Keeper")

        # Create labels and entry fields
        self.website_label = tk.Label(self.root, text="Website:")
        self.website_entry = tk.Entry(self.root, width=30)

        self.username_label = tk.Label(self.root, text="Username:")
        self.username_entry = tk.Entry(self.root, width=30)

        self.password_label = tk.Label(self.root, text="Password:")
        self.password_entry = tk.Entry(self.root, width=30, show="*")

        # Create buttons
        self.add_button = tk.Button(self.root, text="Add", command=self.add_password)
        self.update_button = tk.Button(self.root, text="Update", command=self.update_password)
        self.delete_button = tk.Button(self.root, text="Delete", command=self.delete_password)
        self.retrieve_button = tk.Button(self.root, text="Retrieve", command=self.retrieve_password)

        # Create a listbox to display passwords
        self.password_listbox = tk.Listbox(self.root, width=50)

        # Grid layout
        self.website_label.grid(row=0, column=0, padx=5, pady=5)
        self.website_entry.grid(row=0, column=1, padx=5, pady=5)

        self.username_label.grid(row=1, column=0, padx=5, pady=5)
        self.username_entry.grid(row=1, column=1, padx=5, pady=5)

        self.password_label.grid(row=2, column=0, padx=5, pady=5)
        self.password_entry.grid(row=2, column=1, padx=5, pady=5)

        self.add_button.grid(row=3, column=0, padx=5, pady=5)
        self.update_button.grid(row=3, column=1, padx=5, pady=5)
        self.delete_button.grid(row=3, column=2, padx=5, pady=5)
        self.retrieve_button.grid(row=3, column=3, padx=5, pady=5)

        self.password_listbox.grid(row=4, column=0, columnspan=4, padx=5, pady=5)

        # Bind double-click event on listbox to retrieve password
        self.password_listbox.bind('<Double-Button-1>', self.retrieve_password)

        # Load passwords into the listbox
        self.load_passwords()

    def add_password(self):
        website = self.website_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if website and username and password:
            self.password_keeper.add_password(website, username, password)
            self.clear_entries()
            self.load_passwords()
        else:
            messagebox.showwarning("Warning", "Please enter website, username, and password.")

    def update_password(self):
        website = self.website_entry.get()
        password = self.password_entry.get()

        if website and password:
            self.password_keeper.update_password(website, password)
            self.clear_entries()
            self.load_passwords()
        else:
            messagebox.showwarning("Warning", "Please enter website and password.")

    def delete_password(self):
        website = self.website_entry.get()

        if website:
            self.password_keeper.delete_password(website)
            self.clear_entries()
            self.load_passwords()
        else:
            messagebox.showwarning("Warning", "Please enter the website.")

    def retrieve_password(self, event=None):
        selected_item = self.password_listbox.curselection()
        if selected_item:
            index = selected_item[0]
            website = self.password_listbox.get(index)
            password = self.password_keeper.retrieve_password(website)
            if password:
                messagebox.showinfo("Password", f"The password for {website} is: {password}")
            else:
                messagebox.showwarning("Warning", "Password not found.")
        else:
            messagebox.showwarning("Warning", "Please select a password.")

    def load_passwords(self):
        self.password_listbox.delete(0, tk.END)
        passwords = self.password_keeper.get_passwords()
        for password in passwords:
            self.password_listbox.insert(tk.END, password["website"])

    def clear_entries(self):
        self.website_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def run(self):
        self.root.mainloop()

# Usage example
if __name__ == "__main__":
    password_keeper = PasswordKeeper()  # Assuming you have implemented the PasswordKeeper class
    gui = PasswordKeeperGUI(password_keeper)
    gui.run()
