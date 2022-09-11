import tkinter as tk
import tkinter.font as font


def display_selected():
    choice = var1.get()
    print(choice)
    label1.config(text=choice)

def change_bg(choice):
    label1.config(bg=var2.get())

root =tk.Tk()
root.geometry("300x250")
var1 = tk.StringVar()
var2 = tk.StringVar()
var1.set("Option 1")
var2.set("snow")

menu = tk.OptionMenu(root, var1, "Option 1", "Option 2","Option 3", command=display_selected,)
menu.pack(side="left")
menu2 = tk.OptionMenu(root, var2, "yellow", "red","brown","black","green","grey","orange", command=change_bg,)
menu2.pack(side="right")
menu3 = tk.OptionMenu(root, var2, "GORAB", "PYCR1","PYCR2","ALDH18","SMAD1","SMAD2","NADH", command=change_bg,)
menu3.pack(side="bottom")

label1 = tk.Label(root, text=var1.get(), bg=var2.get())
label1.pack(side="right")

root.mainloop()
