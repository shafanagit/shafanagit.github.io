import FreeSimpleGUI  as FSGUI

def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Display
entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.pack(fill="both", padx=10, pady=10)

# Buttons
frame = tk.Frame(root)
frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill="both")
    
    for btn in row:
        if btn == "=":
            command = calculate
        else:
            command = lambda x=btn: click(x)

        tk.Button(
            row_frame,
            text=btn,
            font=("Arial", 18),
            command=command
        ).pack(side="left", expand=True, fill="both")

# Clear button
tk.Button(
    root,
    text="Clear",
    font=("Arial", 18),
    command=clear
).pack(fill="both", padx=10, pady=10)

root.mainloop()
