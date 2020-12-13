from tkinter import *
import math

def button_clicked():
    miles = int(input.get())
    km = math.floor(miles * 0.6)
    result_label.config(text=km)


window = Tk()
window.title("Miles to KM Calculator")
window.minsize()

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=1, row=0)

#Label
my_label = Label(text="Miles", font=("Arial", 24))
my_label.grid(column=3, row=0)

equal_label = Label(text="is equal to", font=("Arial", 24))
equal_label.grid(column=0, row=1)

result_label = Label(text="", font=("Arial", 24))
result_label.grid(column=1, row=1)

k_label = Label(text="KM", font=("Arial", 24))
k_label.grid(column=2, row=1)

#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)












window.mainloop()
