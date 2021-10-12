def babba(n):
    ab_num=[[0,0] for _ in range(n+1)]
    for i in range(1,n+1):
        if i==1:
            ab_num[i]=[0,1]
        else:
            ab_num[i][0]=ab_num[i-1][1]
            ab_num[i][1]=ab_num[i-1][0]+ab_num[i-1][1]
    return ab_num[i][0],ab_num[i][1]

n=int(input())
a,b=babba(n)
print(a,b)