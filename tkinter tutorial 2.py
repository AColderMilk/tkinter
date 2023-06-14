import tkinter as tk
from tkinter import ttk

def button_func():
    # get content of the entry
    entry_text = entry.get()
    
    # update the label
    # label.configure(text = 'some other text')
    label['text'] = entry_text
    entry['state'] = 'disabled'
    # print(label.configure())

def reset_entry():
    entry['state'] = 'enabled'
    label['text'] = 'some text'

# window
window = tk.Tk()
window.title('Getting and setting widgets')
window.geometry('600x300')

# widgets
label = ttk.Label(master = window, text = 'label')
label.pack()

entry = ttk.Entry(master = window)
entry.pack()

button = ttk.Button(master = window, text = 'Button', 
                    command = button_func)
button.pack()

reset_button = ttk.Button(master = window, text = 'Reset button',
                          command = reset_entry)
reset_button.pack()

# exercise
# add another button that changes text back to some text
# and enables entry again

#run
window.mainloop() 