def rgb_distance(n,price):
    short=[[0,0,0] for _ in range(n+1)]

    num=[-1 for _ in range(n)]
    for i in range(1,n+1):
        short[i][0] = min(short[i-1][1],short[i-1][2]) + price[i-1][0]
        short[i][1] = min(short[i-1][0],short[i-1][2]) + price[i-1][1]
        short[i][2] = min(short[i-1][0],short[i-1][1]) + price[i-1][2]

    return min(short[-1][0], short[-1][1], short[-1][2])
            

n=int(input())
price=[]
for i in range(n):
    tmp=list(map(int, input().split()))
    price.append(tmp)

print(rgb_distance(n,price))
