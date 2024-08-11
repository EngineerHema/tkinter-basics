import tkinter

COLOUR_BG = ("white", "black")
COLOUR_FG = ("black", "white")
all_widgets=[]

window=tkinter.Tk()
window.geometry("400x400")
window.title("Temperature Converter")
window.resizable(False, False)

label=tkinter.Label(text="Choose your input degree", font=("Cosmic", 10))
all_widgets.append(label)
label.pack()

def update_mode():
    bg_color = COLOUR_BG[colour_index.get()]
    fg_color = COLOUR_FG[colour_index.get()]

    window.config(bg=bg_color)

    for widget in all_widgets:
        if isinstance(widget, tkinter.Text) or isinstance(widget, tkinter.Radiobutton) or isinstance(widget, tkinter.Label)  or isinstance(widget, tkinter.Entry) or isinstance(widget, tkinter.Button):
            widget.config(bg=bg_color, fg=fg_color) 


def update_temp():
    temp=float(temperature.get())
    if temp_type.get()=="C":
        result.config(text=f"{temp:.2f} c\n{temp*9/5+32:.2f} f\n{temp+273.15:.2f} k")
    elif temp_type.get()=="F":
        result.config(text=f"{(temp - 32) * 5/9:.2f} c\n{temp:.2f} f\n{(temp - 32) * 5/9 + 273.15:.2f} k")
    else:
        result.config(text=f"{temp - 273.15:.2f} c\n{(temp - 273.15) * 9/5 + 32:.2f} f\n{temp:.2f} k")

    all_widgets.append(result)
    update_mode()
    result.pack()





colour_index = tkinter.IntVar()

colour_index.set(0) 

light_mode = tkinter.Radiobutton(window, text="Light Mode", value=0, variable=colour_index, command=update_mode)
all_widgets.append(light_mode)
light_mode.pack()

dark_mode = tkinter.Radiobutton(window, text="Dark Mode", value=1, variable=colour_index, command=update_mode)
all_widgets.append(dark_mode)
dark_mode.pack()


temp_type = tkinter.StringVar()

temperature=tkinter.Entry()
temperature.focus()
all_widgets.append(temperature)
temperature.pack()

c_temp=tkinter.Radiobutton(window, text="Celesuis", value="C", variable=temp_type, command=update_temp)
c_temp.place(x=0, y=200)
all_widgets.append(c_temp)
f_temp=tkinter.Radiobutton(window, text="Fahrenheit", value="F", variable=temp_type, command=update_temp)
f_temp.place(x=170, y=200)
all_widgets.append(f_temp)
k_temp=tkinter.Radiobutton(window, text="Kelvin", value="K", variable=temp_type, command=update_temp)
k_temp.place(x=330, y=200)
all_widgets.append(k_temp)


result=tkinter.Label()










update_mode()












window.mainloop()