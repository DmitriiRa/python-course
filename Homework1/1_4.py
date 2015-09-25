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
