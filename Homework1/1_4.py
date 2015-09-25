Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:45:13) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
string1 = input()
dic = {}
for i in string1:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
string2 = dic.keys()  
string2 = sorted(string2)     
for i in string2:
    print(i, dic[i])    
