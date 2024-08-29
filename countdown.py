#----------------------------------------------------------------
#
# COUNTDOWN
#
# In this exercise you must create a Graphical User
# Interface using tkinter.  The program should create
# a window containing a label and a button.  The label
# displays a number and each time the button is pressed
# the number in the label should decrease by 1 until
# it reaches zero, at which point some other value can
# be displayed.  This will give you practice at both
# creating widgets and getting them to interact.
#

# Import the necessary tkinter functions
from tkinter import Tk, Button, Label

# Create a window
countdown_window = Tk()

# Give the window a title
countdown_window.title('Countdown')

label_value = 10


##### PUT YOUR CODE HERE

# 1. Define a function to be called when the button is
#    pressed which will change the label's value


def decrement():
    global label_value
    if label_value == 1:
        countdown_label['text'] = 'Go!'
    else:
        label_value -= 1
        countdown_label['text'] = label_value

# 2. Define the Button widget and pack it into the
#    main window


countdown_button = Button(countdown_window, text='Push',
                          font=('Arial', 24, 'bold'), command=decrement())
countdown_button.pack(pady=5)

# 3. Define the Label widget and pack it into the main
#    window

countdown_label = Label(countdown_window, text=str(label_value),
                        font=('Arial', 34, 'bold'))
countdown_label.pack(pady=5)

# Start the event loop to react to user inputs
countdown_window.mainloop()
