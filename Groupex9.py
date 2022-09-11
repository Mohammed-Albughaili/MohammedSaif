import tkinter as tk

def user_choice():
    labelx.config(text = "Type in your sequence, please")

def count_G():
    checking = var.get()
    if checking == "DNA" or checking == "RNA":
        label1.config(text = input1.get().upper().count("G"))
    if checking == "PROTEIN":
        label1.config(text = "This is not possible with a protein sequence")

def count_A():
    checking = var.get()
    if checking == "DNA" or checking == "RNA":
        label2.config(text = input1.get().upper().count("A"))
    if checking == "PROTEIN":
        label2.config(text = "This is not possible with a protein sequence")

def count_C():
    checking = var.get()
    if checking == "DNA" or checking == "RNA":
        label3.config(text = input1.get().upper().count("C"))
    if checking == "PROTEIN":
        label3.config(text = "This is not possible with a protein sequence")

def count_T():
    checking = var.get()
    if checking == "DNA":
        label4.config(text = input1.get().upper().count("T"))
    if checking == "PROTE



root.mainloop()
#tk.Label()
