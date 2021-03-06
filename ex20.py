#LPTHW Exercise 20 Functions and Files

#import argv module
from sys import argv
#unpack argv into variables
script, input_file = argv
#define a function to print the whole file
def print_all(f):
    print(f.read())

#define a function to rewind to the first line of the file
def rewind(f):
    f.seek(0)

#define a function to print a specific line and print the line number and the line
def print_a_line(line_count, f):
    print(line_count, f.readline())

#open the file
current_file = open(input_file)

#print what we will do then call the print whole file method
print("First let's print the whole file:\n")

print_all(current_file)

#print what we will do then call the rewind method
print("Now let's rewind, kind of like a tape.")

rewind(current_file)

#print what we will do then print the three lines individually
print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)