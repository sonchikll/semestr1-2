def f(n):
    s = []
    if n == 1:
        return 1
    while n > 1:
        for i in range (2,n+1):
            if n % i == 0:
                s.append(i)
                n //= i
                break
                
    return s
n = int(input())
print(f(n))

