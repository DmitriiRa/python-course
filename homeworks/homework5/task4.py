import sys
import re


def check(string):
    string = re.findall("\S+", string)
    if (re.match("\.", string[0]) != None):
        return
    if (re.findall("\.\.", string[0]) != []):
        return
    return string


code = sys.stdin.read()

j = 0
data = code.split("\n")
for string in data:
    newstring = string.split("#")[0]
    par = re.findall("(.+) = ", newstring)
    j += 1
    if par != []:
        a = par[0].split(", ")
        print(j, end = " ")
        for i in range(len(a)):
            if check(a[i]) != None:
                print(check(a[i])[0], end = " ")
        print()
