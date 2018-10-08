#LPTHW Exercise 6 Strings and Text
#create variable types_of_people with value of 10 assigned to it
types_of_people = 10
#Use string formatting to add variable into a string stored in variable x
x = f"There are {types_of_people} types of people."
#create variable binary and assign it a string
binary = "binary"
#create variable do_not and assign it a string
do_not = "don't"
#use string formatting to add the above variables in a string and assign it to variable y
y = f"Those who know {binary} and those who {do_not}."
#print variable x
print(x)
#print variable y
print(y)
#print string and add variable x inside using string formatting
print(f"I said: {x}")
#print a string and add variable y inside using string formatting
print(f"I also said: '{y}'")
#assign false to variable hiliarious
hilarious = False
#create variable with string assigned containing space to insert formatting
joke_evaluation = "Isn't that joke so funny?! {}"
#print variable and use .format() method to add another variable
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."
#concatenate the above strings
print(w + e)
