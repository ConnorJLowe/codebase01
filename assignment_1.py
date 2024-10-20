#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment task for QUT's teaching unit
#  IFB104, "Building IT Systems", Semester 2, 2024.  By submitting
#  this code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".

#  Put your student number here as an integer and your name as a
#  character string:

import turtle

student_number = 11969156
student_name = 'Connor Lowe'
#
#  NB: All files submitted for this assessable task will be subjected
#  to automated plagiarism analysis using a tool such as the Measure
#  of Software Similarity (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#


#-----Assessment Task 1 Description----------------------------------#
#
#  This assessment task tests your skills at processing large data
#  sets, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function.  You are required to complete this
#  function so that when the program runs it fills a grid with various
#  symbols, using data stored in a list to determine which symbols to
#  draw and where.  See the online video instructions for
#  full details.
#
#  Note that this assessable assignment is in multiple parts,
#  simulating incremental release of instructions by a paying
#  "client".  This single template file will be used for all parts,
#  and you will submit your final solution as this single Python 3
#  file only, whether you complete all requirements for the
#  assignment.
#
#  This file relies on other Python modules but all of your code
#  must appear in this file only.  You may not change any of the code
#  in the other modules, and you should not submit the other modules
#  with your solution.  The markers will use their own copies of the
#  other modules to test your code, so your solution will not work
#  if it relies on changes made to any other files.
#
#--------------------------------------------------------------------#


#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions used to execute your code.
# You must NOT change any of the code in this section, and you may
# NOT import any non-standard Python modules that need to be
# downloaded and installed separately.
#

# Import standard Python modules needed to complete this assignment.
# You should not need to use any other modules for your solution.
# In particular, your solution must NOT rely on any non-standard
# Python modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.

from turtle import *
from math import *
from random import *
from sys import exit as abort
from os.path import isfile

# Confirm that the student has declared their authorship
if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer), aborting!\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string), aborting!\n')
    abort()

# Import the functions for setting up the drawing canvas
config_file = 'assignment_1_config.py'
if isfile(config_file):
    print('\nConfiguration module found ...\n')
    from assignment_1_config import *
else:
    print(f"\nCannot find file '{config_file}', aborting!\n")
    abort()

# Define the function for generating data sets in Task 1B,
# using the imported raw data generation function if available,
# but otherwise creating a dummy function that just returns an
# empty list
data_file = 'assignment_1_data.py'
if isfile(data_file):
    print('Data generation module found ...\n')
    from assignment_1_data import raw_data


    def data_set(new_seed=randint(0, 99999)):
        return raw_data(new_seed)  # return the random data set
else:
    print('No data generation module available ...\n')


    def data_set(dummy_parameter=None):
        return []

#
#--------------------------------------------------------------------#


#-----Student's Solution---------------------------------------------#

turtle.shape()
#
#  Complete the assignment by replacing the dummy function below with
#  your own function and any other functions needed to support it.
#  All of your solution code must appear in this section.  Do NOT put
#  any of your code in any other sections and do NOT change any of
#  the provided code except as allowed by the comments in the next
#  section.


# All of your code goes in, or is called from, this function.
# In Task 1B ensure that your code does NOT call functions data_set
# or raw_data because they're already called in the main program
# below.

tracer(False)
speed('fastest')


# reusable circle definition
def circle(radius, pen_width, colour, fill_colour):
    turtle.pendown()
    width(pen_width)
    color(colour)
    turtle.fillcolor(fill_colour)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()


def robot(x_coord, y_coord, ori, pop):
    if pop == 'high':
        tracer(False)
        penup()
        goto(x_coord, y_coord)
        color('black')
        width(3)
        turtle.fillcolor('firebrick1')
        turtle.begin_fill()
        pendown()
        triangle_side = 110
        # draw the triangle border
        if ori == 0:
            for i in range(3):
                turtle.forward(110)
                turtle.right(120)
            turtle.end_fill()
        elif ori == 1:
            for i in range(3):
                turtle.forward(110)
                turtle.right(-120)
            turtle.end_fill()
        # center the design
        centroid_x = x_coord + triangle_side / 2
        centroid_y = y_coord - (triangle_side / 6) if ori == 0 else y_coord + (triangle_side / 2)
        turtle.penup()
        turtle.goto(centroid_x - 5, centroid_y - 10)
        # creating the design
        # background shape
        turtle.pendown()
        turtle.color('darkslategray')
        width(2)
        turtle.fillcolor('gray10')
        turtle.begin_fill()
        for i in range(3):
            turtle.forward(9)
            turtle.right(-60)
            turtle.forward(19)
            turtle.right(-60)
        turtle.end_fill()
        # decals
        turtle.penup()
        turtle.goto(centroid_x + 10, centroid_y + 11)
        circle(1, 2, 'darkgrey', 'black')
        turtle.goto(centroid_x - 2, centroid_y + 8)
        circle(2, 2, 'darkgrey', 'black')
        turtle.goto(centroid_x + 7, centroid_y - 2)
        circle(1, 2, 'darkgrey', 'black')
        turtle.goto(centroid_x - 7, centroid_y + 4)
        circle(1, 2, 'darkgrey', 'black')
        # eyes
        turtle.goto(centroid_x, centroid_y + 7)
        circle(5, 1, 'darkgrey', 'red')
        turtle.goto(centroid_x - 3, centroid_y - 5)
        circle(4, 2, 'darkgrey', 'red')
        turtle.goto(centroid_x + 4, centroid_y - 3)
        circle(3, 1, 'darkgrey', 'red')

        # stem down to legs
        turtle.color('black')
        turtle.goto(centroid_x-1, centroid_y-13)
        setheading(270)
        width(5)
        turtle.pendown()
        turtle.forward(10)
        leg_origin = turtle.pos()
        # legs
        width(3)

        # left
        setheading(180)
        turtle.forward(15)
        setheading(220)
        turtle.forward(10)
        setheading(300)
        turtle.forward(10)
        penup()
        goto(leg_origin)

        pendown()
        setheading(190)
        turtle.forward(10)
        setheading(220)
        turtle.forward(15)
        setheading(300)
        turtle.forward(10)
        penup()
        goto(leg_origin)

        pendown()
        setheading(220)
        turtle.forward(15)
        setheading(220)
        turtle.forward(10)
        setheading(300)
        turtle.forward(10)
        penup()
        goto(leg_origin)

        # right
        pendown()
        setheading(315)
        turtle.forward(20)
        setheading(240)
        turtle.forward(14)
        penup()
        goto(leg_origin)

        pendown()
        setheading(335)
        turtle.forward(20)
        setheading(240)
        turtle.forward(14)
        penup()
        goto(leg_origin)

        pendown()
        setheading(0)
        turtle.forward(13)
        setheading(320)
        turtle.forward(10)
        setheading(230)
        turtle.forward(25)
        penup()
        goto(leg_origin)

        setheading(0)
    elif pop == 'low':
        tracer(False)
        penup()
        goto(x_coord, y_coord)
        color('black')
        width(3)
        turtle.fillcolor('darkorange')
        turtle.begin_fill()
        pendown()
        triangle_side = 110
        # draw the triangle border
        if ori == 0:
            for i in range(3):
                turtle.forward(110)
                turtle.right(120)
            turtle.end_fill()
        elif ori == 1:
            for i in range(3):
                turtle.forward(110)
                turtle.right(-120)
            turtle.end_fill()
        # center the design
        centroid_x = x_coord + triangle_side / 2
        centroid_y = y_coord - (triangle_side / 6) if ori == 0 else y_coord + (triangle_side / 2)
        turtle.penup()
        turtle.goto(centroid_x - 5, centroid_y - 10)
        # creating the design
        # background shape
        turtle.pendown()
        turtle.color('darkslategray')
        width(2)
        turtle.fillcolor('gray10')
        turtle.begin_fill()
        for i in range(3):
            turtle.forward(9)
            turtle.right(-60)
            turtle.forward(19)
            turtle.right(-60)
        turtle.end_fill()
        # decals
        turtle.penup()
        turtle.goto(centroid_x + 10, centroid_y + 11)
        circle(1, 2, 'darkgrey', 'black')
        turtle.goto(centroid_x - 2, centroid_y + 8)
        circle(2, 2, 'darkgrey', 'black')
        turtle.goto(centroid_x + 7, centroid_y - 2)
        circle(1, 2, 'darkgrey', 'black')
        turtle.goto(centroid_x - 7, centroid_y + 4)
        circle(1, 2, 'darkgrey', 'black')
        # eyes
        turtle.goto(centroid_x, centroid_y + 7)
        circle(5, 1, 'lightcyan4', 'firebrick4')
        turtle.goto(centroid_x - 3, centroid_y - 5)
        circle(4, 2, 'darkgrey', 'black')
        turtle.goto(centroid_x + 4, centroid_y - 3)
        circle(3, 1, 'darkgrey', 'cadetblue')

        # stem down to legs
        turtle.color('black')
        turtle.goto(centroid_x - 1, centroid_y - 13)
        setheading(270)
        width(5)
        turtle.pendown()
        turtle.forward(10)
        leg_origin = turtle.pos()
        # legs
        width(3)

        # left
        setheading(180)
        turtle.forward(15)
        setheading(220)
        turtle.forward(10)
        setheading(300)
        turtle.forward(10)
        penup()
        goto(leg_origin)

        pendown()
        setheading(190)
        turtle.forward(10)
        setheading(220)
        turtle.forward(15)
        setheading(300)
        turtle.forward(10)
        penup()
        goto(leg_origin)

        pendown()
        setheading(220)
        turtle.forward(15)
        setheading(220)
        turtle.forward(10)
        setheading(300)
        turtle.forward(10)
        penup()
        goto(leg_origin)

        # right
        pendown()
        setheading(315)
        turtle.forward(20)
        setheading(240)
        turtle.forward(14)
        penup()
        goto(leg_origin)

        pendown()
        setheading(335)
        turtle.forward(20)
        setheading(240)
        turtle.forward(14)
        penup()
        goto(leg_origin)

        pendown()
        setheading(0)
        turtle.forward(13)
        setheading(320)
        turtle.forward(10)
        setheading(230)
        turtle.forward(25)
        penup()
        goto(leg_origin)

        setheading(0)
    elif pop == 'clear':
        tracer(False)
        penup()
        goto(x_coord, y_coord)
        # # draw the triangle border
        # if ori == 0:
        #     for i in range(3):
        #         turtle.forward(110)
        #         turtle.right(120)
        #     turtle.end_fill()
        # elif ori == 1:
        #     for i in range(3):
        #         turtle.forward(110)
        #         turtle.right(-120)
        #     turtle.end_fill()
        # center the design
        centroid_x = x_coord + triangle_side / 2
        centroid_y = y_coord - (triangle_side / 6) if ori == 0 else y_coord + (triangle_side / 2)
        turtle.penup()
        turtle.goto(centroid_x - 5, centroid_y - 10)


def display_density(raw_data):
    cell_width = 110
    cell_height = 95
    x_coord = cell_width / 2 - 220
    y_coord = -cell_height
    ori = 0
    pop = 'high'

    # robot(x_coord, y_coord, 1, 'high')
    # robot(x_coord, y_coord, 1, 'high')

    # robot(x_coord, y_coord, 1, 'high')
    moves = ['North', 'East', 'North']

    for move in moves:
        if move == 'North':
            penup()
            if ori == 0:
                y_coord += cell_height * 2
                robot(x_coord, y_coord, 0, pop)
            else:
                robot(x_coord, y_coord, 1, pop)

        elif move == 'East':
            penup()
            if ori == 0:
                x_coord += cell_width / 2
                y_coord -= cell_height
                robot(x_coord, y_coord, 1, pop)
            else:
                x_coord += cell_width / 2
                y_coord += cell_height
                robot(x_coord, y_coord, 0, pop)

        elif move == 'South':
            penup()
            if ori == 0:
                y_coord -= cell_height * 2
                robot(x_coord, y_coord, 1, pop)
            else:
                robot(x_coord, y_coord, 0, pop)

        elif move == 'West':
            penup()
            if ori == 0:
                x_coord -= cell_width / 2
                y_coord += cell_height
                robot(x_coord, y_coord, 1, pop)
            else:
                x_coord -= cell_width / 2
                y_coord -= cell_height
                robot(x_coord, y_coord, 0, pop)


# Key to display meanings of symbols
robot(400, 100, 0, 'high')
robot(500, 0, 1, 'high')

robot(400, -100, 0, 'low')
robot(500, -200, 1, 'low')

#--------------------------------------------------------------------#


#-----Main Program to Run Student's Solution-------------------------#
#

# This main program configures the drawing canvas, calls the student's
# function and closes the canvas.  Do NOT change any of this code
# except as allowed by the comments below.  Do NOT put any of
# your solution code in this section.
#

# Configure the drawing canvas
#
# ***** You can add arguments to this function call to modify
# ***** features of the drawing canvas such as the background
# ***** and line colours, etc
create_drawing_canvas(canvas_title='Density Of Evil Robot Drones Over Earth', write_instructions=False, line_colour='sienna4', background_colour='springgreen4')

goto((grid_width / 2.4) * cell_width, -cell_width / 3)
write('High Population: >500 robots', align='left', font='Arial')
goto((grid_width / 2.4) * cell_width, -cell_width * 2.2)
write('Low Population: 50-500 robots', align='left', font='Arial')

# Create the data set and pass it to the student's function
#
# ***** While developing your Task 1B code you can call the
# ***** "data_set" function with a fixed seed below for the
# ***** random number generator, but your final solution must
# ***** work with "data_set()" as the function call,
# ***** i.e., for any random data set that can be returned by
# ***** the function when called with no seed
display_density(raw_data(12345))  # <-- no argument for "data_set" when assessed

# Exit gracefully
#
# ***** Do not change this function call
release_drawing_canvas(student_name, text_colour='lightblue')

#
#--------------------------------------------------------------------#
