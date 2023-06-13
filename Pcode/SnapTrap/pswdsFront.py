
from tkinter import Tk, Label, Entry, Button, Listbox, Checkbutton, BooleanVar, messagebox as mb, Frame, Scrollbar
import random
import string
from tkinter import messagebox, simpledialog
import tkinter.font as tkfont
from pswdsBend import PasswordKeeper



class StyledListbox(Listbox):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.custom_fonts = {}

    def insert(self, index, *elements, **kwargs):
        font = kwargs.pop('font', None)
        super().insert(index, *elements, **kwargs)
        if font:
            self.custom_fonts[index] = font
            self.itemconfigure(index, font=font)

    def delete(self, first, last=None):
        if isinstance(first, str) and last is None:
            self.custom_fonts.pop(first, None)
        super().delete(first, last)

    def itemconfig(self, index, **kwargs):
        font = kwargs.pop('font', None)
        if font:
            self.custom_fonts[index] = font
        super().itemconfig(index, **kwargs)

class PasswordKeeperGUI:
    def __init__(self, password_keeper):
        self.password_keeper = password_keeper
        self.window = Tk()
        self.window.title("Password Keeper")
        self.window.geometry("385x445")

        self.website_label = Label(self.window, text="Website:", anchor="center")
        self.website_label.pack()
        self.website_entry = Entry(self.window, width=20, justify="center")
        self.website_entry.pack()

        self.username_label = Label(self.window, text="Username:", anchor="center")
        self.username_label.pack()
        self.username_entry = Entry(self.window, width=20, justify="center")
        self.username_entry.pack()

        self.password_label = Label(self.window, text="Password:", anchor="center")
        self.password_label.pack()
        self.password_entry = Entry(self.window, width=20, show="*", justify="center")
        self.password_entry.pack()

        self.show_password_var = BooleanVar()
        self.show_password_checkbox = Checkbutton(self.window, text="Show Password", variable=self.show_password_var,
                                                  command=self.toggle_password_visibility)
        self.show_password_checkbox.pack()

        self.button_frame = Frame(self.window)
        self.button_frame.pack(pady=2)

        self.add_button = Button(self.button_frame, text="Save", command=self.add_password)
        self.add_button.pack(side="left", padx=2, pady=2)

        self.update_button = Button(self.button_frame, text="Update", command=self.update_password)
        self.update_button.pack(side="left", padx=2, pady=2)

        self.delete_button = Button(self.button_frame, text="Delete", command=self.delete_password)
        self.delete_button.pack(side="left", padx=2, pady=2)

        self.button_frame2 = Frame(self.window)
        self.button_frame2.pack(pady=2)

        self.change_pin_button = Button(self.button_frame2, text="Change PIN", command=self.change_pin)
        self.change_pin_button.pack(side="left", padx=2, pady=3)

        self.generate_button = Button(self.button_frame2, text="Randomizer", command=self.generate_password)
        self.generate_button.pack(side="left", padx=2, pady=3)

        self.password_list = StyledListbox(self.window, width=25, height=10, selectmode="single")
        self.password_list.pack()

        self.password_list.bind("<<ListboxSelect>>", self.show_password_entry)

        self.scrollbar = Scrollbar(self.window)
        self.scrollbar.place(x=375, y=0, height=425)

        self.scrollbar.config(command=self.password_list.yview)
        self.password_list.config(yscrollcommand=self.scrollbar.set)

        self.refresh_password_list()

        self.window.mainloop()

    # def change_pin(self):
    #     current_pin = self.ask_pin()
    #     if current_pin is not None and self.password_keeper.check_pin(None, current_pin):
    #         new_pin = simpledialog.askstring("Change PIN", "Enter the new PIN:", show="*")
    #         if new_pin:
    #             self.password_keeper.set_pin(None, new_pin)
    #             mb.showinfo("Success", "PIN updated successfully.")
    #     else:
    #         mb.showwarning("Invalid PIN", "Incorrect PIN. Please try again.")
    def change_pin(self):
        current_pin = self.ask_pin()
        if current_pin is not None and self.password_keeper.check_pin(None, current_pin):
            new_pin = simpledialog.askstring("Change PIN", "Enter the new PIN:", show="*")
            if new_pin:
                self.password_keeper.pin = new_pin  # Update the PIN directly in password_keeper
                mb.showinfo("Success", "PIN updated successfully.")
        else:
            mb.showwarning("Invalid PIN", "Incorrect PIN. Please try again.")

    def generate_password(self):
        password_length = 12
        password_characters = string.ascii_letters + string.digits + string.punctuation
        generated_password = ''.join(random.choice(password_characters) for _ in range(password_length))
        self.password_entry.delete(0, 'end')
        self.password_entry.insert('end', generated_password)
        self.show_password_var.set(False)  # Hide the generated password by default

    def add_password(self):
        website = self.website_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if website and username and password:
            self.password_keeper.add_password(website, username, password)
            self.clear_entry_fields()
            self.refresh_password_list()
        else:
            mb.showwarning("Error", "Please fill in all fields.")

    def update_password(self):
        selected_index = self.password_list.curselection()
        if selected_index:
            selected_password = self.password_list.get(selected_index)
            password_parts = selected_password.split(" | ")
            website = password_parts[0].split(": ")[1]

            new_website = self.website_entry.get()
            new_username = self.username_entry.get()
            new_password = self.password_entry.get()

            if new_website and new_username and new_password:
                if self.password_keeper.update_password(website, new_website, new_username, new_password):
                    mb.showinfo("Success", "Password updated successfully.")
                    self.clear_entry_fields()
                    self.refresh_password_list()
                else:
                    mb.showwarning("Error", "Website not found.")
            else:
                mb.showwarning("Error", "Please fill in all fields.")
        else:
            mb.showwarning("No Selection", "Please select a password to update.")

    def delete_password(self):
        selected_index = self.password_list.curselection()
        if selected_index:
            selected_password = self.password_list.get(selected_index)
            password_parts = selected_password.split(" | ")
            website = password_parts[0].split(": ")[1]

            confirm = mb.askyesno("Confirmation", f"Are you sure you want to delete the password for '{website}'?")
            if confirm:
                if self.password_keeper.delete_password(website):
                    mb.showinfo("Success", "Password deleted successfully.")
                    self.clear_entry_fields()
                    self.refresh_password_list()
                else:
                    mb.showwarning("Error", "Website not found.")
        else:
            mb.showwarning("No Selection", "Please select a password to delete.")

    def clear_entry_fields(self):
        self.website_entry.delete(0, 'end')
        self.username_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')

    def refresh_password_list(self):
        self.password_list.delete(0, 'end')
        passwords = self.password_keeper.get_passwords()

        for website, password_info in passwords.items():
            username = password_info['username']
            item_text = f"\tWebsite: {website}"
            self.password_list.insert('end', item_text)
            self.password_list.insert('end', f"\tUsername: {username}")
            self.password_list.insert('end', '')  # Insert an empty string for spacing

    def ask_pin(self):
        pin = simpledialog.askstring("PIN Required", "Enter the PIN to show the password:", show="*")
        return pin

    def show_password_entry(self, event):
        selected_item = self.password_list.curselection()
        if selected_item:
            index = selected_item[0]
            if index % 3 == 0:  # Check if the selected index is the website index
                website_index = index
                username_index = index + 1
                website = self.password_list.get(website_index)
                username = self.password_list.get(username_index)
                website = website.split(": ")[1]
                username = username.split(": ")[1]
                password_info = self.password_keeper.get_password_info(website)
                decrypted_password = password_info.get('password') if password_info else None
                pin = self.ask_pin()
                if pin is not None and self.password_keeper.check_pin(website, pin):
                    self.clear_entry_fields()
                    self.website_entry.delete(0, 'end')
                    self.website_entry.insert('end', website)
                    self.username_entry.delete(0, 'end')
                    self.username_entry.insert('end', username)
                    self.password_entry.delete(0, 'end')
                    self.password_entry.insert('end', decrypted_password)
                    self.show_password_var.set(False)  # Hide the password by default
                else:
                    mb.showwarning("Invalid PIN", "Incorrect PIN. Please try again.")
        else:
            mb.showwarning("No Selection", "Please select a password entry.")

    def toggle_password_visibility(self):
        show_password = self.show_password_var.get()
        if show_password:
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def center_listbox_text(self):
        # Set the listbox text alignment to center
        self.password_list.configure(justify='center')
        # Set the width of the listbox columns to center-align the text
        self.password_list.columnconfigure(0, weight=1)
        self.password_list.columnconfigure(1, weight=1)

