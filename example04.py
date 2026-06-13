import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

def nic_to_birthdate():
    nic = nic_entry.get().strip().upper()

    try:
        # Old NIC format
        if len(nic) == 10:
            year = 1900 + int(nic[:2])
            day_of_year = int(nic[2:5])

        # New NIC format
        elif len(nic) == 12:
            year = int(nic[:4])
            day_of_year = int(nic[4:7])

        else:
            raise ValueError("Invalid NIC format")

        gender = "Male"

        if day_of_year > 500:
            gender = "Female"
            day_of_year -= 500

        birth_date = datetime(year, 1, 1) + timedelta(days=day_of_year - 1)

        result_text.set(
            f"Birth Date: {birth_date.strftime('%d/%m/%Y')}\n"
            f"Gender: {gender}"
        )

    except Exception:
        messagebox.showerror("Error", "Please enter a valid Sri Lankan NIC number.")

# Create window
root = tk.Tk()
root.title("Sri Lankan NIC Decoder")
root.geometry("350x200")
root.resizable(False, False)

# Title
tk.Label(
    root,
    text="Sri Lankan NIC Decoder",
    font=("Arial", 14, "bold")
).pack(pady=10)

# NIC input
tk.Label(root, text="Enter NIC Number:").pack()
nic_entry = tk.Entry(root, width=25, font=("Arial", 12))
nic_entry.pack(pady=5)

# Button
tk.Button(
    root,
    text="Decode",
    command=nic_to_birthdate,
    font=("Arial", 11)
).pack(pady=10)

# Result
result_text = tk.StringVar()
tk.Label(
    root,
    textvariable=result_text,
    font=("Arial", 12),
    fg="blue"
).pack(pady=10)

root.mainloop()