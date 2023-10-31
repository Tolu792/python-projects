from tkinter import *


def miles_to_kilometer():
    miles = float(user_input.get())
    kilometer = round(miles * 1.60934)
    answer_label.config(text=f"{kilometer}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Entry
user_input = Entry(width=10)
user_input.grid(column=1, row=0)

# Labels
miles_label = Label(text="Miles", font=("Arial", 10, "bold"))
miles_label.grid(column=2, row=0)

equal_to_label = Label(text="is equal to", font=("Arial", 10, "bold"))
equal_to_label.grid(column=0, row=1)

answer_label = Label(text="0", font=("Arial", 10, "bold"))
answer_label.grid(column=1, row=1)

km_label = Label(text="Km", font=("Arial", 10, "bold"))
km_label.grid(column=2, row=1)

# Button
calculate_button = Button(text="Calculate", command=miles_to_kilometer)
calculate_button.grid(column=1, row=2)




window.mainloop()
