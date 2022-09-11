import tkinter as tk
import tkinter.font as font


def ChangeText1(Text):
    w.config(text=Text)
    print(Text)

root = tk.Tk()
myFont = font.Font(size=20)
root.geometry('300x200')
w = tk.Label(root, text="Cutis Laxa!",font=myFont)
w.pack()
button1 = tk.Button(root, text="Cutis Laxa!", command=lambda:ChangeText1("Gerodermia"),font=myFont)
button1.pack()
button2 = tk.Button(root, text="Cutis Laxa!", command=lambda:ChangeText1("PYCR1"),font=myFont)
button2.pack()
root.mainloop()
