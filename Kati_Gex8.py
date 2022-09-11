import tkinter as tk
import re

def ChTxt2():
  new1 = input1.get()
  lista=[]
  listg=[]
  listc=[]
  listt=[]
  listu=[]

  I3 = [m.start() for m in re.finditer("a", new1)]
  for m in I3:
      lista.append(m)
  I3 = [m.start() for m in re.finditer("g", new1)]
  for m in I3:
      listg.append(m)
  I3 = [m.start() for m in re.finditer("c", new1)]
  for m in I3:
      listc.append(m)
  I3 = [m.start() for m in re.finditer("t", new1)]
  for m in I3:
      listt.append(m)
  I3 = [m.start() for m in re.finditer("u", new1)]
  for m in I3:
      listu.append(m)

  A.config(text = len(lista))
  G.config(text = len(listg))
  C.config(text = len(listc))
  T.config(text = len(listt))
  U.config(text = len(listu))

#print("Done")
root = tk.Tk()
input1 = tk.StringVar()
edit1 = tk.Entry(root, textvariable = input1)
edit1.pack()
button1 = tk.Button (root, text ="Type in your nt seq", command = ChTxt2)
button1.pack()
G = tk.Label(root, text ="G count:", height=5, width=20)
G.pack()
A = tk.Label(root, text ="G count:", height=5, width=20)
A.pack()
C = tk.Label(root, text ="G count:", height=5, width=20)
C.pack()
T = tk.Label(root, text ="G count:", height=5, width=20)
T.pack()
U = tk.Label(root, text ="G count:", height=5, width=20)
U.pack()

root.mainloop()
#tk.Label()
