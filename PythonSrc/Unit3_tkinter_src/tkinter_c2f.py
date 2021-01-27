#!/usr/bin/env python3
# Derived from code at http://www.tkdocs.com/tutorial/firstexample.html

import tkinter as tk
from tkinter import ttk


def calculate(*args):
    try:
        celcius = float(celcius_str.get())
        fahrenheit.set((9/5.0) * celcius + 32)
    except ValueError:
        pass

    
root = tk.Tk()
root.title("Celcius to Fahrenheit")
window = ttk.Frame(root, padding="3 3 12 12")


# There are 3 "geometry managers" available:
#   * grid (recommended)
#   * pack (often not flexible enough)
#   * place (often too flexible)
#
# sticky represents which side the grid "sticks" against.
window.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
window.columnconfigure(0, weight=1) # Weight = "stretchability"
window.rowconfigure(0, weight=1)

# Row #1
ttk.Label(window, text="A temperature of").grid(column=1, row=1, sticky=tk.E)
celcius_str = tk.StringVar()
celcius_entry = ttk.Entry(window, width=7, textvariable=celcius_str)  # Width in characters
celcius_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))
ttk.Label(window, text="Celcius").grid(column=3, row=1, sticky=tk.W)

# Row #2
ttk.Label(window, text="is equivalent to").grid(column=1, row=2, sticky=tk.E)
fahrenheit = tk.StringVar()
ttk.Label(window, textvariable=fahrenheit).grid(column=2, row=2, sticky=(tk.W, tk.E))
ttk.Label(window, text="Fahrenheit").grid(column=3, row=2, sticky=tk.W)

# Row #3
ttk.Button(window, text="Calculate", command=calculate).grid(column=3, row=3, sticky=tk.W)

# Set padding for all children of the main window
for child in window.winfo_children():
    child.grid_configure(padx=5, pady=5)

celcius_entry.focus()  # Set cursor to the celcius control.
root.bind('<Return>', calculate)  # Upon <Return> keypress, execute function 'calculate'.
root.bind('<Button-1>', calculate) # Do the same upon mouse click (of button #1)
root.mainloop()
