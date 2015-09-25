Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:45:13) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
s = input().split( )
for i in range(len(s)):
    s[i] = int(s[i])
print(sum(s)/len(s))    
