
import tkinter as tk
import math

# Main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("420x570")
root.resizable(False, False)
root.configure(bg="#202A44")

expression = ""

# Display
display = tk.Entry(
    root, font=("Arial", 22),
    bg="white", fg="black",
    justify="right", bd=10
)
display.pack(fill="x", padx=10, pady=15)

def press(value):
    display.insert(tk.END, value)

def clear():
    display.delete(0, tk.END)

def delete():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])

def calculate():
    try:
        exp = display.get()
        
        # Scientific functions
        exp = exp.replace("√", "math.sqrt")
        exp = exp.replace("log(", "math.log10(")
        exp = exp.replace("ln(", "math.log(")
        exp = exp.replace("sin(", "math.sin(math.radians(")
        exp = exp.replace("cos(", "math.cos(math.radians(")
        exp = exp.replace("tan(", "math.tan(math.radians(")
        
        # Close parentheses for trigonometry
        exp = exp.replace("math.radians(", "math.radians(")
        
        result = eval(exp, {"__builtins__": {}}, {
            "math": math,
            "abs": abs,
            "pow": pow
        })
        
        clear()
        display.insert(0, str(result))

    except Exception:
        clear()
        display.insert(0, "Error")

# Buttons
buttons = [
    ["7", "8", "9", "/", "C"],
    ["4", "5", "6", "*", "DEL"],
    ["1", "2", "3", "-", "+"],
    ["0", ".", "(", ")", "="],
    ["√(", "log(", "ln(", "^", "%"],
    ["sin(", "cos(", "tan(", "π", "e"]
]

def button_click(value):
    if value == "C":
        clear()
    elif value == "DEL":
        delete()
    elif value == "=":
        calculate()
    elif value == "^":
        press("**")
    elif value == "π":
        press("math.pi")
    elif value == "e":
        press("math.e")
    elif value == "%":
        press("/100")
    else:
        press(value)

frame = tk.Frame(root, bg="#202A44")
frame.pack(expand=True, fill="both", padx=8, pady=5)

for row in buttons:
    for item in row:
        btn = tk.Button(
            frame,
            text=item,
            font=("Arial", 14, "bold"),
            bg="#344563",
            fg="white",
            activebackground="#FF9800",
            command=lambda x=item: button_click(x)
        )
        btn.pack(side="left", expand=True, fill="both",
                 padx=3, pady=3)
    # New row
    frame.update_idletasks()
    # Use grid layout instead
    break

# Rebuild buttons using grid
for widget in frame.winfo_children():
    widget.destroy()

for r, row in enumerate(buttons):
    for c, item in enumerate(row):
        btn = tk.Button(
            frame, text=item,
            font=("Arial", 13, "bold"),
            bg="#344563", fg="white",
            activebackground="#FF9800",
            command=lambda x=item: button_click(x)
        )
        btn.grid(row=r, column=c, sticky="nsew",
                 padx=3, pady=3)

for i in range(6):
    frame.grid_rowconfigure(i, weight=1)

for i in range(5):
    frame.grid_columnconfigure(i, weight=1)

root.mainloop()
