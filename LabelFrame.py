import tkinter as tk

root = tk.Tk()
root.geometry('300x200')

label_frame = tk.LabelFrame(root, text = "Genes", labelanchor="n")
label_frame.pack()
var = tk.IntVar()
radio1 = tk.Radiobutton(label_frame, text = "Option1",variable = var, value = 1)
radio1.pack()
radio2 = tk.Radiobutton(label_frame, text = "Option2",variable = var, value = 2)
radio2.pack()
radio3 = tk.Radiobutton(label_frame, text = "Option3",variable = var, value = 3)
radio3.pack()


label_frame1 = tk.LabelFrame(root, text = "Tumers", labelanchor="e")
label_frame1.pack()
var1 = tk.IntVar()
radio1a = tk.Radiobutton(label_frame1, text = "Option1",variable = var1, value = 1)
radio1a.pack()
radio2a = tk.Radiobutton(label_frame1, text = "Option2",variable = var1, value = 2)
radio2a.pack()
radio3a = tk.Radiobutton(label_frame1, text = "Option3",variable = var1, value = 3)
radio3a.pack()


label_frame2 = tk.LabelFrame(root, text = "Cancer", labelanchor="s")
label_frame2.pack()
var2 = tk.IntVar()
radio1b = tk.Radiobutton(label_frame2, text = "Option1",variable = var2, value = 1)
radio1b.pack()
radio2b = tk.Radiobutton(label_frame2, text = "Option2",variable = var2, value = 2)
radio2b.pack()
radio3b = tk.Radiobutton(label_frame2, text = "Option3",variable = var2, value = 3)
radio3b.pack()
root.mainloop()
