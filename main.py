from tkinter import *

def button_clicked():
    try:
        miles = float(miles_input.get()) if miles_input.get() else 0
    except ValueError:
        miles = 0
    kilometers = round(miles * 1.60934, 2)
    converted_to_label.config(text=str(kilometers))

window = Tk()
window.title("Mile to KM Converter")
window.config( padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)
miles_input.config(relief="sunken")

mile_label = Label(text="Miles")
mile_label.grid(column=3, row=0)
miles_label = Label(padx=50, pady=50)

is_equal_label = Label(window, text="is equal to")
is_equal_label.grid(column=0, row=1)

converted_to_label = Label(window, text="0.0")
converted_to_label.grid(column=1, row=1)

km_label = Label(text="KM")
km_label.grid(column=3, row=1)

button = Button(window, text="Calculate", command=button_clicked)
button.grid(column=1, row=2)
button.config(relief="raised")

window.mainloop()