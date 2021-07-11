from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    [password_list.append(random.choice(letters)) for char in range(random.randint(8, 10))]
    [password_list.append(random.choice(symbols)) for char in range(random.randint(2, 4))]
    [password_list.append(random.choice(numbers)) for char in range(random.randint(2, 4))]
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please don't leave any fields empty.")

    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=189, bg="white")
pw_img = PhotoImage(file="logo.png")
canvas.create_image(100, 95, image=pw_img)
canvas.grid(row=0, column=1)

# Labels

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username")
username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

username_input = Entry(width=35)
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(0, "thomas@gmail.com")

password_input = Entry(width=21)
password_input.grid(row=3, column=1)

# Buttons

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
