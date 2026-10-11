a = input().split()
g = int(a[0])
s = a[1]
l = len(s)//g
s1 = ''
for i in range (0,len(s),l):
    s1 += s[i:i+l][::-1]
print(s1)