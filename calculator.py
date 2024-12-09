from tkinter import *
import ast

# Creating the main window
root = Tk()
root.title("Calculator")
root.geometry("600x800")
root.config(bg="#f0f0f0")

# Font styles
button_font = ('Arial', 14)
display_font = ('Arial', 24)

# Writing a function to get button clicked and add it to entry widget
i = 0

def get_number(num):
    global i
    # Insert the num at index i
    display.insert(i, num)
    # Increment the index
    i += 1

def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length

def clear_all():
    display.delete(0, END)

def calculate():
    entire_string = display.get()
    try:
        # Replace 'x²' with '**2' for exponentiation
        entire_string = entire_string.replace('x²', '**2')

        # Compile the expression and evaluate it
        node = ast.parse(entire_string, mode="eval")
        result = eval(compile(node, '<string>', 'eval'))

        # Format result to 2 decimal places for division
        if isinstance(result, float):
            result = round(result, 2)

        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")

def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "")

# Let's first add an input field (Entry widget)
display = Entry(root, font=display_font, bd=10, relief=SOLID, justify=RIGHT, bg="#fff", fg="#333")
display.grid(row=0, column=0, columnspan=4, sticky=W+E, padx=10, pady=20)

# Row 1: x², %, / (divide), Backspace
buttons_row1 = ['x²', '%', '/', '<-']
for col, text in enumerate(buttons_row1):
    Button(root, text=text, font=button_font, width=5, height=2, command=lambda text=text: get_operation(text) if text != '<-' else undo(), bg="#e0e0e0", activebackground="#ccc").grid(row=1, column=col, padx=5, pady=5)

# Row 2: 7, 8, 9, x
buttons_row2 = ['7', '8', '9', 'x']
for col, text in enumerate(buttons_row2):
    Button(root, text=text, font=button_font, width=5, height=2, command=lambda text=text: get_number(text) if text != 'x' else get_operation('*'), bg="#e0e0e0", activebackground="#ccc").grid(row=2, column=col, padx=5, pady=5)

# Row 3: 4, 5, 6, -
buttons_row3 = ['4', '5', '6', '-']
for col, text in enumerate(buttons_row3):
    Button(root, text=text, font=button_font, width=5, height=2, command=lambda text=text: get_number(text) if text not in ['-', 'x'] else get_operation(text), bg="#e0e0e0", activebackground="#ccc").grid(row=3, column=col, padx=5, pady=5)

# Row 4: 1, 2, 3, +
buttons_row4 = ['1', '2', '3', '+']
for col, text in enumerate(buttons_row4):
    Button(root, text=text, font=button_font, width=5, height=2, command=lambda text=text: get_number(text) if text not in ['+', '-', 'x'] else get_operation(text), bg="#e0e0e0", activebackground="#ccc").grid(row=4, column=col, padx=5, pady=5)

# Row 5: AC, 0, ., =
buttons_row5 = ['AC', '0', '.', '=']
for col, text in enumerate(buttons_row5):
    Button(root, text=text, font=button_font, width=5, height=2, command=lambda text=text: clear_all() if text == 'AC' else (get_number(text) if text != '.' else get_operation('.')) if text != '=' else calculate(), bg="#e0e0e0", activebackground="#ccc").grid(row=5, column=col, padx=5, pady=5)

# Start the main loop
root.mainloop()
