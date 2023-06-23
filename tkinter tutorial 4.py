import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.title('buttons')
window.geometry('600x400')

# button
def button_func():
    print('a basic button')

button_string = tk.StringVar(value = 'A Button with StringVar')
button = ttk.Button(window, text = 'A simple button', 
                    command = lambda: print('a basic button')
                    , textvariable = button_string)
button.pack()

# checkbutton
check_var = tk.IntVar(value = 10)
check = ttk.Checkbutton(window, 
                        text = 'checkbox 1',
                        command = lambda: print(check_var.get()),
                        variable = check_var,
                        onvalue = 10,
                        offvalue = 5)
check.pack()

# run
window.mainloop()