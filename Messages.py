import tkinter as tk
import tkinter.font as font


root = tk.Tk()
A1 = "Genius is one percent inspiration, ninety-nine percent perspiration"
#A2 = " You will succeed becuase most people are lazy"
#A3 = " I hope the good moments lasts foreever"
msg = tk.Message(root, text=A1)
msg.config(bg="violet", font=("arial", 28, "italic"))
msg.pack()
root.mainloop()



root = tk.Tk()
A2 = "You will succeed becuase most people are lazy"
msg = tk.Message(root, text=A2)
msg.config(bg="yellow", font=("times", 20, "italic"))
msg.pack()
root.mainloop()


root = tk.Tk()
A3 = "I hope the good moments lasts foreever"
msg = tk.Message(root, text=A3)
msg.config(bg="light blue", font=("times", 30, "italic"))
msg.pack()
root.mainloop()
