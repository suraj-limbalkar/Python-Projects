from tkinter import *

# importing srtftime function to retrive system's time
from time import strftime

# creating tkintner window
root = Tk()
root.title('Suraj\'s Clock')


# time function to display time on the label
def time():
    string = strftime('%I:%M:%S %p')
    # To make the clock format 24 hrs. Simply change the strftime('%I:%M:%S %p') to strftime('%H:%M:%S %p').
    lbl.config(text=string)
    lbl.after(1000, time)  # It will update the time after every (1000 milliseconds i.e. after 1 second)


# Styling the label widget so that clock will look more attractive
lbl = Label(root, font=('calibri', 40, 'bold'), background='purple', foreground='white')


# Placing clock at the centre of the tkinter window
lbl.pack(anchor='center')
time()

mainloop()