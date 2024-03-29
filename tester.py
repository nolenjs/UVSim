import tkinter as tk
from tkinter import filedialog

def load_file():
    filepath = filedialog.askopenfilename()
    if filepath:
        with open(filepath, 'r') as file:
            text_box.delete('1.0', tk.END)
            text_box.insert(tk.END, file.read())

def save_file():
    filepath = filedialog.asksaveasfilename()
    if filepath:
        with open(filepath, 'w') as file:
            file.write(text_box.get('1.0', tk.END))

# Create the main window
root = tk.Tk()
root.title("Simple Text Editor")

# Create a text box
text_box = tk.Text(root, height=20, width=50)
text_box.pack()

# Create the Load button
load_button = tk.Button(root, text="Load", command=load_file)
load_button.pack()

# Create the Save button
save_button = tk.Button(root, text="Save", command=save_file)
save_button.pack()

# Run the application
root.mainloop()