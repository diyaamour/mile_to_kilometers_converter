from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

# Entry

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)


# Labels

miles_label = Label(text="Miles", font=("Arial", 18, "italic"))
miles_label.grid(column=2, row=0)


km_label = Label(text="Km", font=("Arial", 18, "italic"))
km_label.grid(column=2, row=2)


equal_label = Label(text="Is equal to", font=("Arial", 18, "italic"))
equal_label.grid(column=0, row=2)


answer_label = Label(text="", font=("Arial", 18, "italic"))
answer_label.grid(column=1, row=2)


# Button

def calculate_answer():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    answer_label.config(text=f"{km}")


calculate_button = Button(text="Calculate", command=calculate_answer)
calculate_button.grid(column=1, row=3)


window.mainloop()