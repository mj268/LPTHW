#LPTHW Exercise 13 Parameters, Unpacking, Variables

from sys import argv
# read the WYSS section for how to run this
#script, first, second, third = argv

#print("The script is called:", script)
#print("Your first variable is:", first)
#print("Your second variable is:", second)
#print("Your third variable is:", third)

#scriptName, firstVariable, secondVariable = argv

#print("The script is called:", scriptName)
#print("Your first variable is:", firstVariable)
#print("Your second variable is:", secondVariable)

#scriptName2, onlyVariable = argv

#print("The script is called:", scriptName2)
#print("Your first variable is:", onlyVariable)

scriptName, firstArgument = argv

name = input("Tell me your name: ")
print(f"Hello {name} thanks for your arguments")