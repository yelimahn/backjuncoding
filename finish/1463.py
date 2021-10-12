def making_one(num):
    short=[0 for i in range(num+1)]

    for i in range(2,num+1):
        if i==2 or i==3:
            short[i]=1
        else:
            if i%3==0 and i%2==0:
                short[i]=1+min(short[i//3],short[i//2])
            elif i%3==0:
                short[i]=1+min(short[i//3],short[i-1])
            elif i%2==0:
                short[i]=1+min(short[i//2],short[i-1])
            else:
                short[i]=1+short[i-1]

    return short[num]

print(making_one(int(input())))