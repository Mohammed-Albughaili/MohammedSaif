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
root, text="Yemen", variable=var, value="Yemen", command=ShowChoice,
)
radio1.pack(anchor="w")
radio2 = tk.Radiobutton(
root, text="Sanaa", variable=var, value="Sanaa", command=ShowChoice,
)
radio2.pack(anchor="w")
radio3 = tk.Radiobutton(
root, text="Taiz", variable=var, value="Taiz", command=ShowChoice,
)
radio3.pack(anchor="w")
radio4 = tk.Radiobutton(
root, text="Aden", variable=var, value="Aden", command=ShowChoice,
)
radio4.pack(anchor="w")
radio5 = tk.Radiobutton(
root, text="Hajaa", variable=var, value="Hajaa", command=ShowChoice,
)
radio5.pack(anchor="w")
radio6 = tk.Radiobutton(
root, text="IBB", variable=var, value="IBB", command=ShowChoice,
)
radio6.pack(anchor="w")

root.mainloop()


# var1 = tk.StringVar()
# var2 = tk.StringVar()
# var1.set("Option 1")
# var2.set("snow")
#
# menu = tk.OptionMenu(root, var1, "Option 1", "Option 2","Option 3", command=display_selected,)
# menu.pack(side="left")
# menu2 = tk.OptionMenu(root, var2, "yellow", "red","brown","black","green","grey","orange", command=change_bg,)
# menu2.pack(side="right")
# menu3 = tk.OptionMenu(root, var2, "GORAB", "PYCR1","PYCR2","ALDH18","SMAD1","SMAD2","NADH", command=change_bg,)
# menu3.pack(side="bottom")
#
# label1 = tk.Label(root, text=var1.get(), bg=var2.get())
# label1.pack(side="right")


#
