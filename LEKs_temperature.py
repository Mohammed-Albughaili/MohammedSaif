import tkinter as tk
import tkinter.font as font



def convert_temperature():
    input_choice = input_conversion_type.get()
    output_choice = output_conversion_type.get()

    value = input1.get()
    result = 0
    print("Convert from:" + input_choice)
    print("Convert to:" + output_choice)

    print("Input Value:" + str(value))

    # °C ==> K, °C ==> °F, K ==> °C, K ==> °F, °F ==> K and °F ==> °C

    if input_choice == "Fahrenheit" and output_choice == "Celsius": #°F ==> °C
        result = (5/9) * (value - 32)

    if input_choice == "Kelvin" and output_choice == "Celsius": #K ==> °C
        result = value - 273.15

    if input_choice == "Celsius" and output_choice == "Fahrenheit": #°C ==> °F
        result = value * (9/5) + 32

    if input_choice == "Kelvin" and output_choice == "Fahrenheit": # K ==> °F
        result = 9/5 * (value - 273) + 32

    if input_choice == "Fahrenheit" and output_choice == "Kelvin": #F ==> K
        result = (value + 459.67) * 5/9

    if input_choice == "Celsius" and output_choice == "Kelvin": # °C ==> K,
        result = (value) + 273.15

        print("Value is " + str(result) + " from " + input_choice +" to " + output_choice +" of " + str(value))

    label2.config(text=result)


root =tk.Tk()
root.geometry("300x250")
input_conversion_type = tk.StringVar()
output_conversion_type = tk.StringVar()

value = tk.StringVar()
input_conversion_type.set("Fahrenheit")
output_conversion_type.set("Celsius")

input1 = tk.IntVar()
label1 = tk.Label(root, text="Input")
label1.pack(side="top")
edit1 = tk.Entry(root, textvariable = input1)
edit1.pack(side="top")

menuInput = tk.OptionMenu(root, input_conversion_type, "Fahrenheit", "Kelvin", "Celsius")
menuInput.pack(side="top")

label1 = tk.Label(root, text="Output")
label1.pack(side="left")

menuOutput = tk.OptionMenu(root, output_conversion_type, "Fahrenheit", "Kelvin", "Celsius")
menuOutput.pack(side="left")

label2 = tk.Label(root, text="0")
label2.pack(side="right")

Button1 = tk.Button(root, text="Convert", command=convert_temperature)
Button1.pack(side="bottom")

root.mainloop()
