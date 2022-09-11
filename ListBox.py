import tkinter as tk

def items_selected(event):
        selected_index = listbox.get(listbox.curselection())
        print("You selected:", selected_index)


root = tk.Tk()
root.geometry("200x400")
root.resizable(False, False)
#myFont = font.Font(size=20)
root.title("Listbox")
langs = ["sanaa","Ibb","Taiz","Aden","Hajaa","Lahj","Hudida","Dhamar","Maareb","Radaa"]
langs_var = tk.StringVar(value=langs)
listbox = tk.Listbox(root,listvariable=langs_var,height=9)
#listbox.bind("<<ListboxSelected>>", items_selected)
listbox.pack()
root.mainloop()
