def fib_0_1(n):
    fib=[[] for _ in range(n+1)]
    for i in range(0,n+1):
        if i==0:
            fib[i]=[1,0]
        elif i==1:
            fib[i]=[0,1]
        else:
            fib[i].append(fib[i-1][0]+fib[i-2][0])
            fib[i].append(fib[i-1][1]+fib[i-2][1])
    return fib[n]

t=int(input())
out=[]
for i in range(t):
    n=int(input())
    out.append(fib_0_1(n))
for j in range(t):
    print("%d %d" %(out[j][0],out[j][1]))