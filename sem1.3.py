A = list(map(float, input().split()))
s = 1
for i in range (len(A)):
    s = s * A[i]
print(s**(1/len(A)))