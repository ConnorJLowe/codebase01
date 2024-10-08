#---------------------------------------------------------------------#
#
# Morlock Finder
#
# This exercise gives you some practice at find patterns in a large
# amount of text, using both Python's "find" method and regular
# expressions.  The text in this case is the pioneering science fiction
# novel, "The Time Machine", by H. G. Wells.  This is contained in a
# plain text file, TheTimeMachine.txt, which is divided into individual
# lines separated by newline markers.
#
# In the first task you will iterate over each line in the file one
# at a time.  All of the other tasks use a copy of the file's entire
# contents which has been read as a single (very long) string
# containing embedded newline markers.
#

from re import findall

# Task 1: The bad guys in the novel are the evil, underground-dwelling
# Morlocks.  Add a for-each loop to the following code and
# use the "find" method to find and print each line of the
# novel that mentions Morlocks.
# time_machine = open('TheTimeMachine.txt') # open the file
#
# for line in time_machine:
#     if 'Morlock' in line:
#         print(line)
#
#
# time_machine.close() # close the file

# Read the file's contents into a character string.  You should
# use this string to complete all of the tasks below, so don't
# change it.
time_machine = open('TheTimeMachine.txt') # open the file
time_machine_text = time_machine.read() # read the file's contents
time_machine.close() # close the file

# Task 2: The heroine is called Weena, one of a tribe of devolved human
# beings living in the distant future.  Using the "find" method and a
# while loop, print all the locations in the novel where Weena's name is
# mentioned.

# location = time_machine_text.find('Weena')
#
# while location != -1:
#     print(location)
#     location = time_machine_text.find('Weena', location + 1)


# Task 3: Rather than using loops and repeated calls to "find", the
# "findall" function provides a much easier way to find all occurrences
# of a pattern.  Use the findall function to print how many times
# Weena's name appears in the novel.  Hint: This can be done very
# concisely by applying the built-in "len" function to the result
# returned by findall.

# matches = findall('Weena', time_machine_text)
# print(len(matches))
    
# Task 4: In this plain text version of the novel emphasis has been indicated
# by surrounding words with underscores, e.g., "_nil_".  Use the
# findall function and an appropriate regular expression to find and
# print all individual emphasised words in the novel's text.  Do not print the
# underscores.

# regex = '_([A-Za-z]+)_'
#
# matches = findall(regex, time_machine_text)
# print(matches)


# Task 5: The file contains many hyphenated words and phrases, e.g., "re-use".
# Use the findall function and an appropriate regular expression to find and
# print all phrases in the file containing a single hyphen. Ensure that you
# allow for both upper and lower case letters in the phrase.

regex = '[A-Za-z]+-[A-Za-z]+'
matches = findall(regex, time_machine_text)
print(matches)
