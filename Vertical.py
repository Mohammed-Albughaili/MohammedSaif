import tkinter as tk
import tkinter.font as font


def show1():
    sel = "Vertical Scale Value = " + str(v1.get())
    label2.config(text=sel,)


root = tk.Tk()
root.geometry("300x400")
v1 = tk.DoubleVar()
scale1 = tk.Scale(root, variable=v1, from_=1, to=200, orient="vertical")
label1 = tk.Label(root, text="Vertical Scaler")
button1 = tk.Button(text="Display Vertical", command=show1, bg="red")
label2 = tk.Label(root)
scale1.pack(anchor="center")
label1.pack()
button1.pack(anchor="center")
label2.pack()
root.mainloop()
