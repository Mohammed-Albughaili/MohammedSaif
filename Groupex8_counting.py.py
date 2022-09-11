import tkinter as tk
import tkinter.font as font
import re

def count_G():
    label1.config(text = input1.get().upper().count("G"))

root = tk.Tk()

input1 = tk.StringVar()
edit1 = tk.Entry(root, textvariable = input1)
edit1.pack()

button1 = tk.Button(root, text = "Please Click to count G!", command = count_G)
button1.pack()

label1 = tk.Label(root, text =" please give  anumber")
label1.pack()


root.mainloop()
