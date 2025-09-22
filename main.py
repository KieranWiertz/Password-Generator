import random
import tkinter as tk
from tkinter import messagebox

letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = list("!#$%&()*+")

def generate_password():
    try:
        userLetters = int(letter_entry.get())
        userNumbers = int(number_entry.get())
        userSymbols = int(symbol_entry.get())

        passwordList = (
            random.choices(letters, k=userLetters)
            + random.choices(numbers, k=userNumbers)
            + random.choices(symbols, k=userSymbols)
        )

        random.shuffle(passwordList)
        password = ''.join(passwordList)

        result_label.config(text=f"Your password: {password}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# --- UI Setup ---
root = tk.Tk()
root.title("🔑Password Generator🔑")
root.geometry("350x250")

tk.Label(root, text="How many letters?").pack()
letter_entry = tk.Entry(root)
letter_entry.pack()

tk.Label(root, text="How many numbers?").pack()
number_entry = tk.Entry(root)
number_entry.pack()

tk.Label(root, text="How many symbols?").pack()
symbol_entry = tk.Entry(root)
symbol_entry.pack()

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), fg="white")
result_label.pack()

root.mainloop()
