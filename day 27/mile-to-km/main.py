from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)

input = Entry()
input.config(width=10)
input.grid(column=1, row=0)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)

value = Label(text="0")
value.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)


def button_clicked():
    print("I got clicked")
    v = int(input.get())
    v = round(v * 1.609)
    value.config(text=v)


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
