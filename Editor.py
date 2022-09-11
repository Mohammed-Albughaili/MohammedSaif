import tkinter as tk
import tkinter.font as font


def Text_Output():
    text1.inser(1.0, "This is a Test\n")
    Content = text1.get(1.0, "end")
    label1.config(text="you pressed the first button")
    print(Content)
    print(repr(Content))



def Text_Clear():
    label1.config(text="you pressed the second button")
    text1.delete(1.0, "end")
def Text_Printout():
    label1.config(text="you pressed the third button")

def  Text_length():
    label1.config(text="you pressed the fourth button")
def Text_Display():
    label1.config(text="you pressed the fivth button")


root = tk.Tk()
text1 = tk.Text(root, background="red")
text1.pack()

button1 = tk.Button(root, text="Insert text field", command=Text_Output, width=30, font=15 )
button1.pack(side="bottom")
button2 = tk.Button(root, text="Get content", command=Text_Clear, width=30, font=15 )
button2.pack(side="left")
button3 = tk.Button(root, text="Display text length", command=user_change_1, width=30, font=15 )
button3.pack(side="bottom")
button4 = tk.Button(root, text="Clear text field", command=user_change_1, width=30, font=15 )
button4.pack(side="right")
button5 = tk.Button(root, text="Print out of text", command=Text_Printout, width=30, font=15 )
button5.pack(side="bottom")


root.mainloop()
