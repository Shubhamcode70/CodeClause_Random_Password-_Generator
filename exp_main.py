from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import string

def generate_password():
    pwd_length = 8

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    nums = string.digits
    syms = string.punctuation

    all_chars = lower + upper + nums + syms
    # rg = random.sample(all_chars, pwd_length)
    # print("a".join(rg))
    password = "".join(random.sample(all_chars, pwd_length))
    return password

def copy_clipboard():
    password = password_entry.get()
    pyperclip.copy(password)

def save_password():
    username = username_entry.get()
    password = password_entry.get()
    print(password)

    with open('password_data.txt', 'r') as file:
        password_info = file.readlines()

    if any(f"Username : {username}" in line for line in password_info):
        messagebox.showinfo("Warning", "Username Already Exist")
    else:
        with open('password_data.txt', 'a') as file:
            file.write(f"Username : {username} \t")
            file.write(f"Password : {password} \n")
            messagebox.showinfo("Saved", "Username & Password Saved")

window = Tk()
window.title("Password Generator Using Python")
window.config(pady=100, padx=100, bg="skyblue")

username_label = Label(window, text="Username:",bg="skyblue")
username_label.pack(padx=5, pady=5)
username_entry = Entry(window, width=50)
username_entry.pack()
password_label = Label(window, text="Password:", bg="skyblue")
password_label.pack(padx=5, pady=5)

password_entry = Entry(window, width=50)
password_entry.pack()
# display_lbl = Label(text="", relief="sunken", height=1, width=50, highlightcolor="black", highlightthickness="2")
# display_lbl.pack(pady=5, padx=5)

generate_button = Button(window, text="Generate Password",bg="red", fg="white", command=lambda:password_entry.insert(0, generate_password()))
generate_button.pack(pady=10, padx=10)
copy_button = Button(window, text="Copy Password", command=copy_clipboard)
copy_button.pack()
save_button = Button(window, text="Save Password", command=save_password)
save_button.pack()

window.mainloop()
