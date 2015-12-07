import re
import sys


data = sys.stdin.read()
i = 0
code = data.split("\n")
for string in code:
    par = re.findall("(\w+) = ", string)
    i += 1
    if par != []:
        print(i, par[0])
