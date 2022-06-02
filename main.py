import string
import tkinter as t
import pyperclip
from tkinter import messagebox


def generate_random_password():
    import random

    letters = string.ascii_letters
    numbers = string.digits
    symbols = "".join(["!", "#", "$", "&", "(", ")", "*", "+"])

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letters_list = [random.choice(letters) for _ in range(nr_letters)]
    symbols_list = [random.choice(symbols) for _ in range(nr_symbols)]
    numbers_list = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = letters_list + symbols_list + numbers_list

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, t.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def save_data():

    website_info = website_input.get()
    user_info = email_input.get()
    password = password_entry.get()

    if len(website_info) > 0 and len(user_info) > 0 and len(password) > 0:

        is_okey = messagebox.askokcancel(
            title=website_info,
            message=f"These are the details entered:\nUser Info: {user_info}\nPassword: {password}\nIs it okey to save?",
        )
        if is_okey:
            with open(file="data.txt", mode="a") as file:
                file.write(f"{website_info} | {user_info} | {password}\n")
            website_input.delete(0, t.END)
            password_entry.delete(0, t.END)
            website_input.focus()
    else:
        messagebox.showwarning(
            title="Oops", message="Please don't leave any fields empty!"
        )


window = t.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = t.Canvas(width=200, height=200, highlightthickness=0)
logo = t.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = t.Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = t.Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = t.Label(text="Password:")
password_label.grid(row=3, column=0)

website_input = t.Entry(width=50)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

email_input = t.Entry(width=50)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "barankircaa@gmail.com")

password_entry = t.Entry(width=32)
password_entry.grid(row=3, column=1)

generate_button = t.Button(text="Generate Password", command=generate_random_password)
generate_button.grid(row=3, column=2)

add_button = t.Button(width=36, text="Add", command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
