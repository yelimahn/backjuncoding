def fib_num(n):
    fib=[0 for _ in range(n+1)]
    for i in range(n+1):
        if i==0 or i==1:
            fib[i]=i
        else:
            fib[i]=fib[i-1]+fib[i-2]
    return fib[n]

n=int(input())
print(fib_num(n))        