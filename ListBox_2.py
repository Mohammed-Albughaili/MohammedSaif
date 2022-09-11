import tkinter as tk
import tkinter.font as font


def items_selected():
    language =[]
    selected_indices = listbox.curselection()
    for i in selected_indices:
        index = listbox.get(i)
        language.append(index)
    for lang in language:
        print("You selected:", lang)



root = tk.Tk()
root.geometry("200x400")
root.resizable(False, False)
#myFont = font.Font(size=20)
root.title("Listbox")
langs = ["sanaa","Ibb","Taiz","Aden","Hajaa","Lahj","Hudida","Dhamar","Maareb","Radaa"]
langs_var = tk.StringVar(value=langs)
listbox = tk.Listbox(
    root,
    listvariable=langs_var,
    height=10,
    selectmode="multiple",
    selectbackground="green",
    selectforeground="blue",
)
#listbox.bind("<<ListboxSelected>>", items_selected)
button1 = tk.Button(text="Click Me", command=items_selected)
listbox.pack(fill="both")
button1.pack()
root.mainloop()
