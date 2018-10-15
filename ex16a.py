#LPTHW Study Drill Ex16
#Read from ex16 created file

from sys import argv

script, filename = argv
#txt = open("/Users/markjuniper/Development/Python/LPTHW/someText")
txt = open(filename)
print(txt.read())
