import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def _init_(self, root):  # Corrected constructor method
        self.root = root
        self.root.title("Password Generator")
        
        # UI Elements
        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=10, pady=10)
        self.length_entry = tk.Entry(root)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.include_uppercase = tk.BooleanVar()
        self.uppercase_check = tk.Checkbutton(root, text="Include Uppercase", variable=self.include_uppercase)
        self.uppercase_check.grid(row=1, column=0, columnspan=2)
        
        self.include_numbers = tk.BooleanVar()
        self.numbers_check = tk.Checkbutton(root, text="Include Numbers", variable=self.include_numbers)
        self.numbers_check.grid(row=2, column=0, columnspan=2)
        
        self.include_special = tk.BooleanVar()
        self.special_check = tk.Checkbutton(root, text="Include Special Characters", variable=self.include_special)
        self.special_check.grid(row=3, column=0, columnspan=2)
        
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=4, column=0, columnspan=2, pady=10)
        
        self.password_label = tk.Label(root, text="Generated Password:")
        self.password_label.grid(row=5, column=0, padx=10, pady=10)
        self.password_display = tk.Entry(root)
        self.password_display.grid(row=5, column=1, padx=10, pady=10)
    
    def generate_password(self):
        length = self.length_entry.get()
        if not length.isdigit():
            messagebox.showerror("Error", "Password length must be a number")
            return
        length = int(length)
        
        characters = string.ascii_lowercase
        if self.include_uppercase.get():
            characters += string.ascii_uppercase
        if self.include_numbers.get():
            characters += string.digits
        if self.include_special.get():
            characters += string.punctuation
        
        if length < 1 or length > 128:
            messagebox.showerror("Error", "Password length must be between 1 and 128")
            return
        
        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_display.delete(0, tk.END)
        self.password_display.insert(0, password)

if _name_ == "_main_":  # Corrected main condition
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
