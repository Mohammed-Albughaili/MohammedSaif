import tkinter as tk


# def add_up():
#     Nr1 = input1.get()
#     Nr2 = input2.get()
#     result = float(Nr1) + float(Nr2)
#     w.config(text=str(result))

def Changelabel1():
    label1.config(text= "I have new Text")

def Changelabel2():
    label2.config(text= "empty")

def user_change_1():
    label1.config(text= input1.get())
def user_change_2():
        label1.config(text= input2.get())

root = tk.Tk()
input1 = tk.StringVar()
input2 = tk.StringVar()
edit1 = tk.Entry(root, textvariable=input1, font=12, width=25)
edit2 = tk.Entry(root, textvariable=input2, font=12, width=25)
edit1.pack()
edit2.pack()
label1 = tk.Label(root, text = "live")
label2 = tk.Label(root, text = "death")
label3 = tk.Label(root, text = "world")
label1.pack()
label2.pack()
label3.pack()
#w = tk.Label(root, text="Genetics disorders!")
#w.pack()
button1 = tk.Button(root, text="Click Me", command=user_change_1, width=30, font=15 )
button1.pack()
button2 = tk.Button(root, text="Press the button", command=user_change_1, width=30, font=15 )
button2.pack()
#Button1 = tk.Label(root, text="Chronic Inflammatory diseases!")
#Button1.pack()
# w = tk.Label(root, text="Press the button", font=12, width=25)
#w.pack
root.mainloop()
