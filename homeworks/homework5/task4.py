import sys
import re


def check(string):
    string = re.findall("\S+", string) # избавились от пробелов и табуляции
    if (re.match("\.", string[0]) != None): # отбросили слова начинающиеся с "."
        return
    if (re.findall("\.\.", string[0]) != []): # отбросили слова с ".."
        return
    return string


f = open('temp.txt', 'w')
a = sys.stdin.read()
f.write(a) 
f.close()


with open("temp.txt") as f: 
    j = 0
    data = f.read().split("\n")
    for string in data:
        newstring = string.split("#")[0]
        par = re.findall("(.+) = ", newstring) # par - все  что перед =
        j += 1
        if par != []: # если в строке есть присвоение
            a = par[0].split(", ") # разбили строку по запятым
            print(j, end = " ")
            for i in range(len(a)): 
                if check(a[i]) != None:
                    print(check(a[i])[0], end = " ")
            print()
            
