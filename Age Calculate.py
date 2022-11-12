
from tkinter import *
from tkinter import messagebox



age_app = Tk()


# Change app Text
age_app.title("Calculate Age App")


# set Demensions
age_app.geometry("400x200")


# Write Age Label
the_text = Label(age_app, text ="Write Your Age", height=2, font=("Arial",20))
the_text.pack()  # place The Text Into The Main Window


# Age Variables
age = StringVar()

# Set Default Value For Age
age.set("00")

# Create The Input For Age
age_input = Entry(age_app, width=10, font=("Arial",30), textvariable= age)
age_input.pack()  # place The Input Into The Main Window

# Create The Function Calc

def calc():
    # Get Age In Years
    the_age_value = age.get()
    # Get Time Units
    months = int(the_age_value) * 12
    weeks = months * 4
    days = int(the_age_value) * 365

    line_one = f"Your Age In Months Is: {months}"
    line_two = f"Your Age In Weeks Is: {weeks}"
    line_three = f"Your Age In Days Is: {days}"

    all_lines = [line_one,line_two,line_three]

    messagebox.showinfo("Your Age In All Times Units", "\n".join(all_lines))

# Create The Calculate Buttons
btn = Button(age_app, text="Calculate Age", width=20,
             height=2 , bg="#e91e63",fg="white",borderwidth=0,command=calc)

btn.pack()  # place The Button Into The Main Window



age_app.mainloop()

