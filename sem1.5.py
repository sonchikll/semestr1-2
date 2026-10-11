N = int(input())
b = int(input())
c = int(input())

l = int(str(N),b)
s = ''
k = 0
while l!=0:
    s = str(l%c) + s
    l = l//c
    k = k+1

for i in range (k) :
    print(s[i],sep='',end='')