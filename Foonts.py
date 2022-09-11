import tkinter as tk
import tkinter.font as font

root = tk.Tk()

myFont = font.Font(family="Bitstream", slant="italic", size=28, underline=1)
myFont2 = font.Font(family="Serif", size=15, underline=1)
myFont3 = font.Font(family="Arial", size=20, underline=1)

label1 = tk.Label(root, text="Genetics disorders!", font=myFont)
label1.pack()
label2 = tk.Label(root, text="Cutis Laxa Syndrom!", font=myFont2)
label2.pack()
label3 = tk.Label(root, text="Gerodermia Osteoplastica!", font=myFont3)
label3.pack()

root.mainloop()
