from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import json

FONT_NAME = "Arial"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
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

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    passw_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    web = website_entry.get()
    email = email_entry.get()
    passw = passw_entry.get()

    new_data = {
        web: {
            "email": email,
            "password": passw
        }
    }

    if len(web) < 3 or len(email) < 4 or len(passw) < 5:
        messagebox.showinfo(title="Warning", message="Check your input")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"These are details entered: \nEmail: {email}\n "
                                                          f"Password: {passw}\n Is it ok to save?")

        if is_ok:
            try:
                with open("data.json", "r") as file:
                    # Reading old data
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as file:
                    # Saving the data
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                passw_entry.delete(0, END)


# ---------------------------- SEARCH ------------------------------- #
def find_password():
    website_name = website_entry.get()

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="ERROR", message=f"No data file found")
    else:
        if website_name in data:
            email = data[website_name]["email"]
            password = data[website_name]["password"]
            messagebox.showinfo(title=website_name, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="ERROR", message=f"No details for {website_name} exists.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=(FONT_NAME, 12, "normal"))
website_label.grid(column=0, row=1)
website_entry = Entry(width=23)
website_entry.focus()
website_entry.grid(column=1, row=1)

search_button = Button(text="Search", command=find_password, font=(FONT_NAME, 10, "normal"), width=16)
search_button.grid(column=2, row=1)

email_label = Label(text="Email/Username:", font=(FONT_NAME, 12, "normal"))
email_label.grid(column=0, row=2)
email_entry = Entry(width=43)
email_entry.insert(0, "@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

passw_label = Label(text="Password:", font=(FONT_NAME, 12, "normal"))
passw_label.grid(column=0, row=3)
passw_entry = Entry(width=23)
passw_entry.grid(column=1, row=3)
passw_button = Button(text="Generate Password", command=generate_password, font=(FONT_NAME, 10, "normal"))
passw_button.grid(column=2, row=3)

add_button = Button(text="Add", command=save_pass, font=(FONT_NAME, 10, "normal"), width=38)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
