from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


my_label = Label(text="I am a label", font=("Arial", 24))
my_label.pack()
text_label = ''

def button_clicked():
    print("I got clicked")
    my_label["text"] = input.get()

# Entry
input = Entry(width=10)
input.pack()


button = Button(text = "Click Me", command=button_clicked)
button.pack()





window.mainloop()

