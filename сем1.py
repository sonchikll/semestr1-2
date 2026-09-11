
#1
a = float(input())
b = float(input())
print(a+b,a-b,a*b)


#2
c = int(input())
print(c%10)


#3
A = list(map(float, input().split()))
s = 1
for i in range (len(A)):
    s = s * A[i]
print(s**(1/len(A)))



#5
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

