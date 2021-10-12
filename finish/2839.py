def sugar_deliver(n):
    short=[0 for _ in range(n+1)]
    for i in range(1,n+1):
        if i==1 or i==2:
            short[i]=-1
        elif i<=5:
            if i==3 or i==5:
                short[i]=1
            else:
                short[i]=-1
        else:
            if short[i-3]==-1 and short[i-5]==-1:
                short[i]=-1
            elif short[i-3]==-1:
                short[i]=1+short[i-5]
            elif short[i-5]==-1:
                short[i]=1+short[i-3]
            else:
                short[i]=1+min(short[i-3],short[i-5])
    return short[n]

n=int(input())
print(sugar_deliver(n))