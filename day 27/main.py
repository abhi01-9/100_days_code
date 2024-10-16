from tkinter import *

window = Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.pack(side = "left") # it can be bottom and right
# my_label.pack(expand = True) # to keep in center

my_label["text"] = "new Text"
my_label.config(text="New Text")
my_label.config(padx=50, pady=50)
my_label.grid(column=0, row=0)


# Button

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)
# Entry
input = Entry()
input.config(width=10)
input.grid(column=3, row=2)

window.mainloop()
