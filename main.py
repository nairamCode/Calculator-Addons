from tkinter import *
class calculator():
    def run():
        window = Tk()
        window.title('Calculator')
        window.configure(width=263, height=399)
        # Text Field
        field = Label(state='disabled', width=32, height=7).place(x=0, y=0)
        # Operations
        plus_button = Button(text="+", width=8, height=3).place(x=198, y=288)
        minus_button = Button(text="-", width=8, height=3).place(x=198, y=232)
        multiplication_button = Button(text="*", width=8, height=3).place(x=198, y=176)
        division_button = Button(text=":", width=8, height=3).place(x=198, y=120)
        equals_button = Button(text="=", width=8, height=3).place(x=198, y=344)
        # Numbers
        number_one_button = Button(text="1", width=8, height=3).place(x=0, y=288)
        number_two_button = Button(text="2", width=8, height=3).place(x=66, y=288)
        number_three_button = Button(text="3", width=8, height=3).place(x=132, y=288)
        number_four_button = Button(text="4", width=8, height=3).place(x=0, y=232)
        number_five_button = Button(text="5", width=8, height=3).place(x=66, y=232)
        number_six_button = Button(text="6", width=8, height=3).place(x=132, y=232)
        number_seven_button = Button(text="7", width=8, height=3).place(x=0, y=176)
        number_eight_button = Button(text="8", width=8, height=3).place(x=66, y=176)
        number_nine_button = Button(text="9", width=8, height=3).place(x=132, y=176)
        window.mainloop()

calculator.run()