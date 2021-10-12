n=int(input())
stair=[0 for _ in range(n)]
for i in range(n):
    stair[i]=int(input())

output=[[0,0] for _ in range(n)]
for i in range(n):
    if i==0:
        output[i][0]=stair[i]
    elif i==1:
        output[i][0]=output[i-1][0]+stair[i]
        output[i][1]=1
    elif i==2:
        if stair[i-1]>stair[i-2]:
            output[i][0]=stair[i-1]+stair[i]
            output[i][1]=1
        else:
            output[i][0]=stair[i-2][0]+stair[i]
    else:
        if output[i-1][1]==1:#2
            if output[i-3][0]+stair[i-1] > output[i-2][0]:
                output[i][0]=output[i-3][0]+stair[i-1]+stair[i]
                output[i][1]=1
            else:
                output[i][0]=output[i-2][0]+stair[i]
        else:
            output[i][0]=max(output[i-1][0],output[i-3][0]+stair[i-1],output[i-2][0])+stair[i]
            if output[i][0]!=output[i-2][0]:
                output[i][1]=1

print(output[n-1][0])