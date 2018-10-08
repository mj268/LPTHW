#LPTHW Exercise 5 More Variables and Printing

my_name = 'Zed A. Shaw'
my_age = 35 #not a lie
my_height = 74 #inches
my_weight = 180 #lbs
my_eyes = 'blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print(f"Actually that's not too heavy")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")

# Study drills

name = 'Mark'
age = 35 #not a lie
height = 74 #inches
height_in_cm = height * 2.54
weight = 180 #lbs
weight_in_kg = 180 * 0.45359237
eyes = 'green'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"His height in cm is {height_in_cm}.")
print(f"He's {weight} pounds heavy.")
print(f"His weight in kg is {weight_in_kg}.")
print(f"Actually that's not too heavy")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
