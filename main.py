import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
 
 
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pasword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
 
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
 
    password_list = []
 
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
 
    password_list = password_symbols + password_letters + password_numbers
 
    random.shuffle(password_list)
 
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
 
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # gets the item entered in the dialog box
    website = website_entry.get()
    email = email_and_username_entry.get()
    password = password_entry.get()
 
    new_data = {
 
        website: {
            "email": email,
            "password":password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure that you haven't left any fields empty.")
 
    else:
        try:
            with open("data.json", "r") as data_file:
                # writes and saves data to the text file
                password_data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:

            password_data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(password_data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            email_and_username_entry.delete(0,END)
 
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


 
 
# ---------------------------- UI SETUP ------------------------------- #
 
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
 
canvas = Canvas(width=200, height=200)
pic = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pic)
canvas.grid(row=0, column=1)
 
# Labels
website_label = Label(text="Website")
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
website_label.grid(row=1, column=0)
password_label = Label(text="Password")
password_label.grid(row=3, column=0)
 
# Entry
website_entry = Entry(width=26)
website_entry.grid(row=1, column=1)
website_entry.focus()
password_entry = Entry(width=26)
password_entry.grid(row=3, column=1)
email_and_username_entry = Entry(width=47)
email_and_username_entry.grid(row=2, column=1, columnspan=3)
# Buttons
generate_password_button = Button(text="Generate Password", command=generate_pasword)
generate_password_button.grid(row=3, column=2, columnspan=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=5, column=1, columnspan=2)
search_button = Button(text="Search", width=12, command=find_password)
search_button.grid(row=1, column=3)
 
window.mainloop()