import tkinter as tk
import tkinter.font as font

def DisplayChoice():
    if i == 1:
        text = "Current Value1: " + str(spinbox1.get())
        label.configure(text = text1)
        return(0)
    if i == 2:
        text = "Current Value2: " + str(spinbox2.get())
        label.configure(text = text1)
        return(0)
    if i == 3:
        text = "Current Value3: " + str(spinbox3.get())
        label.configure(text = text1)
        return(text1)


root = tk.Tk()
frame = tk.Frame(root, width = 200, height = 80)
values = ["Sanaa", "Aden", "Ibb", "Taiz", "Lahj", "Maareb"]
spinbox1 = tk.Spinbox(root, from_ = 0, to = 10,increment = 1,command = lambda: DisplayChoice(i))
spinbox2 = tk.Spinbox(root, from_ = 0, to = 10,increment = 1,command = lambda: DisplayChoice)
spinbox3 = tk.Spinbox(
root, from_ = 0, to = 10,increment = 1, values = values,command = lambda: DisplayChoice)
spinbox1.pack()
spinbox2.pack()
spinbox3.pack()
text1 = "Current Value: " + str(spinbox1.get())
label = tk.Label(root, text = text1)
label.pack()
button1 = tk.Button(root, text="Display Choice", command= lambda:DisplayChoice)
button1.pack()
frame.pack(padx = 10, pady = 10, expand = True, fill = tk.BOTH)

#text1 = "Current Value: " + str(spinbox1.get())
label1 = tk.Label(root, text = text1)
label.pack()
button1 = tk.Button(root, text="Display Choice", command= lambda:DisplayChoice)
button1.pack()
frame.pack(padx = 10, pady = 10, expand = True, fill = tk.BOTH)

#text2 = "Current Value: " + str(spinbox2.get())
label2 = tk.Label(root, text = text1)
label2.pack()
button2 = tk.Button(root, text="Display Choice", command= lambda: DisplayChoice)
button2.pack()
frame.pack(padx = 10, pady = 10, expand = True, fill = tk.BOTH)

#text3 = "Current Value: " + str(spinbox3.get())
label3 = tk.Label(root, text = text1)
label3.pack()
button3 = tk.Button(root, text="Display Choice", command=DisplayChoice)
button3.pack()
frame.pack(padx = 10, pady = 10, expand = True, fill = tk.BOTH)

root.mainloop()
