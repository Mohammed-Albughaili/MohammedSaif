import tkinter as tk
import tkinter.font as font


def ShowChoice():
    print(var.get())

root =tk.Tk()
var = tk.StringVar()
var.set("Yemen")
label1 = tk.Label(root, text="Pick up of the follwing")
label1.pack()

radio1 = tk.Radiobutton(
    root,
    text="Yemen",
    variable=var,
    value="Yemen",
    command=ShowChoice,
    indicator=0,
    width=30,
)
radio1.pack(anchor="w")
radio2 = tk.Radiobutton(
    root,
    text="Sanaa",
    variable=var,
    value="Sanaa",
    command=ShowChoice,
    indicator=0,
    width=30,
)
radio2.pack(anchor="w")
radio3 = tk.Radiobutton(
    root,
    text="Taiz",
    variable=var,
    value="Taiz",
    command=ShowChoice,
    indicator=0,
    width=30,
)
radio3.pack(anchor="w")
radio4 = tk.Radiobutton(
    root,
    text="Aden",
    variable=var,
    value="Aden",
    command=ShowChoice,
    indicator=0,
    width=30,
)
radio4.pack(anchor="w")
radio5 = tk.Radiobutton(
    root,
    text="Hajaa",
    variable=var,
    value="Hajaa",
    command=ShowChoice,
    indicator=0,
    width=30,
)
radio5.pack(anchor="w")
radio6 = tk.Radiobutton(
    root,
    text="IBB",
    variable=var,
    value="IBB",
    command=ShowChoice,
    indicator=0,
    width=30,
)
radio6.pack(anchor="w")

root.mainloop()
