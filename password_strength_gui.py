import tkinter as tk
from tkinter import messagebox
import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) < 8:
        feedback.append("Too short (min 8 characters).")
    elif len(password) >= 12:
        score += 2
    else:
        score += 1

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Use both uppercase and lowercase.")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    if re.search(r'[@$!%*?&^#_~\-]', password):
        score += 1
    else:
        feedback.append("Include a special character.")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, feedback

def on_check():
    password = entry.get()
    strength, suggestions = check_password_strength(password)

    result_label.config(text=f"Strength: {strength}", fg="green" if strength == "Strong" else "orange" if strength == "Moderate" else "red")

    tips_text = "\n".join(f"- {tip}" for tip in suggestions) if suggestions else "Looks good!"
    suggestions_label.config(text=tips_text)

# GUI setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")
root.resizable(False, False)

tk.Label(root, text="Enter your password:", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root, width=30, show="*", font=("Arial", 12))
entry.pack()

check_btn = tk.Button(root, text="Check Strength", command=on_check, font=("Arial", 11))
check_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack()

suggestions_label = tk.Label(root, text="", wraplength=360, justify="left", font=("Arial", 10))
suggestions_label.pack(pady=10)

root.mainloop()
