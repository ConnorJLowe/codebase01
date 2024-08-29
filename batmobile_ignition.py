#----------------------------------------------------------------
#
# BATMOBILE IGNITION 
#
# In this exercise you will use radio buttons to control the
# text in a label.
#
# The scenario: Here you will emulate part of the Batmobile's
# dashboard display from the 1966 "Batman" television show.
# In each episode Batman and Robin would leap into the
# nuclear-powered Batmobile and Robin would read the ignition
# status from the dashboard:
#
#     "Atomic batteries to 'Power'. Turbines to 'Speed'."
#
# Upon hearing this, Batman would always reply:
#
#     "Roger. Ready to move out."
#
# The Batmobile would then roar out of the Batcave for the
# 14 mile journey from stately Wayne Manor to Gotham City.
#
# In this exercise you will create two pairs of radio buttons,
# one for the atomic batteries' status and one for the turbines'
# status.  A text label will display the state of the Batmobile,
# which should be "Ready" only when the buttons are in the
# configuration described by Robin above.  See the instructions
# accompanying this file for full details.
#
# Notes:
# 1) For neatness we have put the radio buttons into LabelFrame
#    widgets in our final version, but you need not bother
#    with the frames in your first attempt.
# 2) Only one radio button from a group can be selected at a time.
#    All buttons that refer to the same variable are part of
#    the same group.
# 3) The LabelFrame widget has an optional 'text' parameter which
#    can be used to give a name to the frame.
#

# Import the necessary tkinter functions
from tkinter import Tk, LabelFrame, Label, BooleanVar, Radiobutton

###### CREATE YOUR SOLUTION BY REPLACING THE 'pass' STATEMENTS BELOW

# 1. Create a Tk window
dashboard = Tk()

# 2. Give the window a title
dashboard.title('Batmobile Ignition')

# 3. Create a Label widget to displays the Batmobile's
# ignition status (initially "Waiting...")
ignition_status = Label(dashboard, text='Waiting...', font=('Arial', 42), fg='red', pady=(300))

# 4. Introduce two Boolean variables, whose values will be changed
# by selecting radio buttons, for the atomic batteries' and turbines'
# statuses, respectively

batteries_ready = BooleanVar()
turbines_ready = BooleanVar()


# 5. Define a function to change the label's text when the right
# radio buttons are selected

def update_status():
    battery_is_ready = batteries_ready.get()
    turbine_is_ready = turbines_ready.get()

    if battery_is_ready and turbine_is_ready == True:
        ignition_status['text'] = 'Ready!'
        ignition_status['fg'] = 'green'
    else:
        ignition_status['text'] = 'Waiting...'
        ignition_status['fg'] = 'red'


# 6. Create two LabelFrame widgets to hold the pairs of radio
# buttons (unlike Frames, LabelFrames have a 'text' attribute)
battery_frame = LabelFrame(dashboard, text='Atomic Batteries',
                           font=('Arial', 20))

turbine_frame = LabelFrame(dashboard, text='Turbines',
                           font=('Arial', 20))

# 7. Create two radio button widgets within the batteries frame,
# labelled 'Charging' and 'Power', both referring to the same
# Boolean variable
Charging_RB = Radiobutton(battery_frame, text='Charging',
                          font=('Arial', 20),
                          variable=batteries_ready,
                          value=False,
                          command=update_status)
Power_RB = Radiobutton(battery_frame, text='Power',
                       font=('Arial', 20),
                       variable=batteries_ready,
                       value=True,
                       command=update_status)

# 8. Create two radio button widgets within the turbines frame,
# labelled 'Idle' and 'Speed', both referring to the same
# Boolean variable
Idle_RB = Radiobutton(turbine_frame, text='Idle',
                      font=('Arial', 20),
                      variable=turbines_ready,
                      value=False)

Speed_RB = Radiobutton(turbine_frame, text='Speed',
                       font=('Arial', 20),
                       variable=turbines_ready,
                       value=True)

# 9. Use the grid geometry manager to put the four radio buttons
# into their frames (each on a separate row and sticking to the
# West border)
Charging_RB.grid(row=1, column=1, sticky='w')
Power_RB.grid(row=2, column=1, sticky='w')

Idle_RB.grid(row=1, column=1, sticky='w')
Speed_RB.grid(row=2, column=1, sticky='w')

# 10. Use the grid geometry manager to put the three main widgets
# into the root window
ignition_status.grid(row=1, column=1, columnspan=2, rowspan=2)

battery_frame.grid(row=2, column=1, padx=5, pady=5)
turbine_frame.grid(row=2, column=2, padx=5, pady=5)

# 11. Start the event loop to react to user inputs
dashboard.mainloop()
