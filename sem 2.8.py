n = int(input())
A = list(map(int,input().split()))
for j in range (n-1):
    for i in range(1,n):
        if A[i] < A[i-1]:
            A[i], A[i-1] = A[i-1], A[i]
print(A)
print(A[n//2])