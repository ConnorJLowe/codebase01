#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item for QUT's teaching unit
#  IFB104, "Building IT Systems", Semester 2, 2024.  By submitting
#  this code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#  Put your student number here as an integer and your name as a
#  character string:
#
student_number = 11969156
student_name = 'Connor Lowe'
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#


#-----Assessment Task 2 Description----------------------------------#
#
#  In this assessment task you will combine your knowledge of Python
#  programming, HTML-style mark-up languages, pattern matching,
#  database management, and Graphical User Interface design to produce
#  a robust, interactive "app" that allows its user to view and save
#  data from multiple online sources.
#
#  See the client's briefings accompanying this file for full
#  details.
#
#  Note that this assessable assignment is in multiple parts,
#  simulating incremental release of instructions by a paying
#  "client".  This single template file will be used for all parts,
#  together with some non-Python support files.
#
#--------------------------------------------------------------------#


#-----Set up---------------------------------------------------------#
#
# This section imports standard Python 3 modules sufficient to
# complete this assignment.  Don't change any of the code in this
# section, but you are free to import other Python 3 modules
# to support your solution, provided they are standard ones that
# are already supplied by default as part of a normal Python/IDLE
# installation.
#
# However, you may NOT use any Python modules that need to be
# downloaded and installed separately, such as "Beautiful Soup" or
# "Pillow", because the markers will not have access to such modules
# and will not be able to run your code.  Only modules that are part
# of a standard Python 3 installation may be used.

# A function for exiting the program immediately (renamed
# because "exit" is already a standard Python function).
from sys import exit as abort

# A function for opening a web document given its URL.
# [You WILL need to use this function in your solution,
# either directly or via the "download" function below.]
from urllib.request import urlopen

# Some standard Tkinter functions.  [You WILL need to use
# SOME of these functions in your solution.]  You may also
# import other widgets from the "tkinter" module, provided they
# are standard ones and don't need to be downloaded and installed
# separately.  (NB: Although you can import individual widgets
# from the "tkinter.tkk" module, DON'T import ALL of them
# using a "*" wildcard because the "tkinter.tkk" module
# includes alternative versions of standard widgets
# like "Label" which leads to confusion.  If you want to use
# a widget from the tkinter.ttk module name it explicitly,
# as is done below for the progress bar widget.)
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Progressbar

# Functions for finding occurrences of a pattern defined
# via a regular expression.  [You do not necessarily need to
# use these functions in your solution, because the problem
# may be solvable with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.]
from re import *

# A function for displaying a web document in the host
# operating system's default web browser (renamed to
# distinguish it from the built-in "open" function for
# opening local files).  [You WILL need to use this function
# in your solution.]
from webbrowser import open as urldisplay

# All the standard SQLite database functions.  [You WILL need
# to use some of these in your solution.]
from sqlite3 import *

#
#--------------------------------------------------------------------#


#-----Validity Check-------------------------------------------------#
#
# This section confirms that the student has declared their
# authorship.  You must NOT change any of the code below.
#

if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer)\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string)\n')
    abort()


#
#--------------------------------------------------------------------#


#-----Supplied Function----------------------------------------------#
#
# Below is a function you can use in your solution if you find it
# helpful.  You are not required to use this function, but it may
# save you some effort.  Feel free to modify the function or copy
# parts of it into your own code.
#

# A function to download and save a web document.  The function
# returns the downloaded document as a character string and
# optionally saves it as a local file.  If the attempted download
# fails, an error message is written to the shell window and the
# special value None is returned.  However, the root cause of the
# problem is not always easy to diagnose, depending on the quality
# of the response returned by the web server, so the error
# messages generated by the function below are indicative only.
#
# Parameters:
# * url - The address of the web page you want to download.
# * target_filename - Name of the file to be saved (if any).
# * filename_extension - Extension for the target file, usually
#      "html" for an HTML document or "xhtml" for an XML
#      document.
# * save_file - A file is saved only if this is True. WARNING:
#      The function will silently overwrite the target file
#      if it already exists!
# * char_set - The character set used by the web page, which is
#      usually Unicode UTF-8, although some web pages use other
#      character sets.
# * incognito - If this parameter is True the Python program will
#      try to hide its identity from the web server. This can
#      sometimes be used to prevent the server from blocking access
#      to Python programs. However we discourage using this
#      option as it is both unreliable and unethical to
#      override the wishes of the web document provider!
#
def download(url='http://www.wikipedia.org/',
             target_filename='downloaded_document',
             filename_extension='html',
             save_file=True,
             char_set='UTF-8',
             incognito=False):
    # Import the function for opening online documents and
    # the class for creating requests
    from urllib.request import urlopen, Request

    # Import an exception sometimes raised when a web server
    # denies access to a document
    from urllib.error import HTTPError

    # Import an exception raised when a web document cannot
    # be downloaded due to some communication error
    from urllib.error import URLError

    # Open the web document for reading (and make a "best
    # guess" about why if the attempt fails, which may or
    # may not be the correct explanation depending on how
    # well behaved the web server is!)
    try:
        if incognito:
            # Pretend to be a web browser instead of
            # a Python script (not recommended!)
            request = Request(url)
            request.add_header('User-Agent',
                               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; ' + \
                               'rv:91.0; ADSSO) Gecko/20100101 Firefox/91.0')
            print("Warning - Request to server does not reveal client's true identity.")
            print("          Use this option only if absolutely necessary!\n")
        else:
            # Behave ethically
            request = url
        web_page = urlopen(request)
    except ValueError as message:  # probably a syntax error
        print(f"\nCannot find requested document '{url}'")
        print(f"Error message was: {message}\n")
        return None
    except HTTPError as message:  # possibly an authorisation problem
        print(f"\nAccess denied to document at URL '{url}'")
        print(f"Error message was: {message}\n")
        return None
    except URLError as message:  # probably the wrong server address
        print(f"\nCannot access web server at URL '{url}'")
        print(f"Error message was: {message}\n")
        return None
    except Exception as message:  # something entirely unexpected
        print("\nSomething went wrong when trying to download " + \
              f"the document at URL '{str(url)}'")
        print(f"Error message was: {message}\n")
        return None

    # Read the contents as a character string
    try:
        web_page_contents = web_page.read().decode(char_set)
    except UnicodeDecodeError as message:
        print("\nUnable to decode document from URL " + \
              f"'{url}' as '{char_set}' characters")
        print(f"Error message was: {message}\n")
        return None
    except Exception as message:
        print("\nSomething went wrong when trying to decode " + \
              f"the document from URL '{url}'")
        print(f"Error message was: {message}\n")
        return None

    # Optionally write the contents to a local text file
    # (silently overwriting the file if it already exists!)
    if save_file:
        try:
            text_file = open(f'{target_filename}.{filename_extension}',
                             'w', encoding=char_set)
            text_file.write(web_page_contents)
            text_file.close()
        except Exception as message:
            print(f"\nUnable to write to file '{target_filename}'")
            print(f"Error message was: {message}\n")

    # Return the downloaded document to the caller
    return web_page_contents


#
#--------------------------------------------------------------------#


#-----Student's Solution---------------------------------------------#

# Create the main window
main = Tk()
main_font = ('Roman', 30, 'bold')
main_font_s = ('Courier', 20, 'italic')
main.title('Top 3 Businesses')

import time


def update_time():
    current_time = time.strftime("%H:%M:%S | %d/%m/%Y")
    time_label.config(text=current_time)
    main.after(1000, update_time)


def update_main():
    inbox.config(text=f'Selected: {cat_selection.get()}')


cat_selection = StringVar(value='None')

cover_image = PhotoImage(file='stock-top2.png')
image_label = Label(main, image=cover_image)
title = Label(main, text='The "Top 3" Public Businesses', fg='green', font=('Small Fonts', 30))
time_label = Label(main, fg='black', font=('System', 20), padx=0, pady=0)
update_time()

category_buttons = LabelFrame(main, relief='groove', font=main_font, borderwidth=3, text='Business Categories')
rank_buttons = LabelFrame(main, relief='groove', font=main_font, borderwidth=3, text='Save a Ranking?')
messages = LabelFrame(main, relief='groove', font=main_font, borderwidth=3, text='Messages')

# displays the 3 categories of business
valuation_button = Radiobutton(category_buttons, text='Company Valuation', variable=cat_selection, value='Valuation', font=main_font, command=update_main)
roi_button = Radiobutton(category_buttons, text='Return on Investment', variable=cat_selection, value='ROI', font=main_font, command=update_main)
profit_button = Radiobutton(category_buttons, text='Net Profit', variable=cat_selection, value='Profit', font=main_font, command=update_main)
top_three_button = Button(category_buttons, text='Show Top Three', font=('Roman', 15), width=22)
source_button = Button(category_buttons, text='Show Data Source', font=('Roman', 15), width=22)

# displays ability to save which top business to save
first_button = Button(rank_buttons, text='First', font=main_font, width=15)
second_button = Button(rank_buttons, text='Second', font=main_font, width=15)
third_button = Button(rank_buttons, text='Third', font=main_font, width=15)

# message box
inbox = Label(messages, text=f'Selected: {cat_selection.get()}', fg='black', font=main_font_s, width=20, height=8)

valuation_button.grid(row=1, sticky='w')
roi_button.grid(row=2, sticky='w')
profit_button.grid(row=3, sticky='w')
top_three_button.grid(row=4, sticky='w')
source_button.grid(row=4, sticky='e')

first_button.grid(row=1, sticky='w')
second_button.grid(row=2, sticky='w')
third_button.grid(row=3, sticky='w')

inbox.grid(row=1, sticky='w')

margin = 5

time_label.grid(padx=margin, pady=50, row=0, column=3)
messages.grid(padx=margin, pady=margin, row=2, column=3, columnspan=25)
image_label.grid(row=0, column=1, columnspan=2)
title.grid(row=1, column=1, columnspan=2)
category_buttons.grid(padx=margin, pady=margin, row=2, column=1)
rank_buttons.grid(padx=margin, pady=margin, row=2, column=2)

main.mainloop()