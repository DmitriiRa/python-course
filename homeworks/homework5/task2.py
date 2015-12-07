import re
import sys

numbers = sys.stdin.read()

allnumbers = numbers.split("\n")
for number in allnumbers:
    if re.findall("0{3}|1{3}|2{3}|3{3}|4{3}|5{3}|6{3}|7{3}|8{3}|9{3}", number)
    != []:
        print(number)
