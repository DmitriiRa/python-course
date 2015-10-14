s = input().split()
s1 = []
s2 = []

for i in range(len(s)):
    a = int(s[i])
    if i % 2 == 0:
        s1.append(a)
    else:
        s2.append(a)

s1 = sorted(s1)
s2 = sorted(s2)
s2.reverse()

# print(s1)
# print(s2)

if len(s) % 2 == 1:
    a = s1.pop()

s3 = []
for i in range(len(s2)):
    s3.append(s1[i])
    s3.append(s2[i])
