import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, decrypt=False):
    result = ""
    shift = -shift if decrypt else shift

    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def encrypt_text():
    try:
        shift = int(shift_entry.get())
        text = input_text.get("1.0", tk.END).strip()
        encrypted = caesar_cipher(text, shift)
        output_text.config(state=tk.NORMAL)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, encrypted)
        output_text.config(state=tk.DISABLED)
    except ValueError:
        messagebox.showerror("Invalid Shift", "Please enter a valid integer for shift.")

def decrypt_text():
    try:
        shift = int(shift_entry.get())
        text = input_text.get("1.0", tk.END).strip()
        decrypted = caesar_cipher(text, shift, decrypt=True)
        output_text.config(state=tk.NORMAL)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, decrypted)
        output_text.config(state=tk.DISABLED)
    except ValueError:
        messagebox.showerror("Invalid Shift", "Please enter a valid integer for shift.")

def clear_all():
    input_text.delete("1.0", tk.END)
    shift_entry.delete(0, tk.END)
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.config(state=tk.DISABLED)

def exit_app():
    root.destroy()

# GUI Setup
root = tk.Tk()
root.title("Caesar Cipher Encryption/Decryption")
root.geometry("600x450")
root.configure(bg="#f0f4f7")

title = tk.Label(root, text="Caesar Cipher", font=("Helvetica", 20, "bold"), bg="#f0f4f7", fg="#2b2d42")
title.pack(pady=10)

frame = tk.Frame(root, bg="#f0f4f7")
frame.pack(pady=10)

# Input text
tk.Label(frame, text="Enter Text:", font=("Helvetica", 12), bg="#f0f4f7").grid(row=0, column=0, sticky="w")
input_text = tk.Text(frame, height=5, width=60)
input_text.grid(row=1, column=0, columnspan=4, padx=10, pady=5)

# Shift
tk.Label(frame, text="Shift Value:", font=("Helvetica", 12), bg="#f0f4f7").grid(row=2, column=0, sticky="w", padx=10, pady=5)
shift_entry = tk.Entry(frame, width=10)
shift_entry.grid(row=2, column=1, pady=5, sticky="w")

# Buttons
btn_frame = tk.Frame(root, bg="#f0f4f7")
btn_frame.pack(pady=10)

encrypt_btn = tk.Button(btn_frame, text="Encrypt", font=("Helvetica", 12), bg="#4CAF50", fg="white", width=10, command=encrypt_text)
encrypt_btn.grid(row=0, column=0, padx=10)

decrypt_btn = tk.Button(btn_frame, text="Decrypt", font=("Helvetica", 12), bg="#2196F3", fg="white", width=10, command=decrypt_text)
decrypt_btn.grid(row=0, column=1, padx=10)

clear_btn = tk.Button(btn_frame, text="Clear", font=("Helvetica", 12), bg="#FFC107", fg="black", width=10, command=clear_all)
clear_btn.grid(row=0, column=2, padx=10)

exit_btn = tk.Button(btn_frame, text="Exit", font=("Helvetica", 12), bg="#f44336", fg="white", width=10, command=exit_app)
exit_btn.grid(row=0, column=3, padx=10)

# Output
tk.Label(root, text="Output:", font=("Helvetica", 12), bg="#f0f4f7").pack()
output_text = tk.Text(root, height=5, width=70, state=tk.DISABLED)
output_text.pack(pady=5)

root.mainloop()
