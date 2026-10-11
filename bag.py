W = int(input())
n = int(input()) #количество
p = [1,2,3] #стоимость
w = [1,2,3] #масса
P = [[0 for j in range(W+1)] for i in range (n+1)]

for k in range (1,n+1):
    for s in range (1, W+1):
        if w[k-1] <= s:
            P[k][s] = max(p[k-1] + P[k-1][s-w[k-1]], P[k-1][s])
        else:
            P[k][s] = P[k-1][s]
        
s = W
k = n
a = []
while s*k > 0:
    if P[k][s] != P[k-1][s]:
        a.append(k)
        s -= w[k-1]
    k -= 1
print (P, P[-1][-1],a)