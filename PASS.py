import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    include_lowercase = lowercase_var.get()
    include_uppercase = uppercase_var.get()
    include_digits = digits_var.get()
    include_special_chars = special_chars_var.get()

    chars = ''
    if include_lowercase:
        chars += string.ascii_lowercase
    if include_uppercase:
        chars += string.ascii_uppercase
    if include_digits:
        chars += string.digits
    if include_special_chars:
        chars += string.punctuation

    if chars == '':
        password_entry.delete(0, tk.END)
        password_entry.insert(0, "Select at least one character type.")
        return

    passwords = []
    for _ in range(num_passwords.get()):
        password = ''.join(random.choice(chars) for _ in range(length))
        passwords.append(password)

    password_entry.delete(0, tk.END)
    password_entry.insert(0, "\n".join(passwords))
    pyperclip.copy("\n".join(passwords))

# GUI setup
root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

lowercase_var = tk.IntVar()
lowercase_check = tk.Checkbutton(root, text="Include lowercase letters", variable=lowercase_var)
lowercase_check.pack()

uppercase_var = tk.IntVar()
uppercase_check = tk.Checkbutton(root, text="Include uppercase letters", variable=uppercase_var)
uppercase_check.pack()

digits_var = tk.IntVar()
digits_check = tk.Checkbutton(root, text="Include digits", variable=digits_var)
digits_check.pack()

special_chars_var = tk.IntVar()
special_chars_check = tk.Checkbutton(root, text="Include special characters", variable=special_chars_var)
special_chars_check.pack()

num_passwords = tk.IntVar()
num_passwords.set(1)
num_passwords_label = tk.Label(root, text="Number of passwords to generate:")
num_passwords_label.pack()

num_passwords_entry = tk.Entry(root, textvariable=num_passwords)
num_passwords_entry.pack()

generate_button = tk.Button(root, text="Generate Password(s)", command=generate_password)
generate_button.pack()

password_entry = tk.Entry(root, show="")
password_entry.pack()

root.mainloop()
