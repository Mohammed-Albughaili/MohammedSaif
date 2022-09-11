import tkinter as tk


def ChangeText1():
    w.config(text="I have new Text", background="blue")
    print("I did changes")

root = tk.Tk()
w = tk.Label(root, text="Genetics disorders!")
w.pack()
Button1 = tk.Button(root, text="Acute Inflammatory diseases!", command=ChangeText1)
Button1.pack()
Button1 = tk.Label(root, text="Chronic Inflammatory diseases!")
Button1.pack()

w.mainloop()
