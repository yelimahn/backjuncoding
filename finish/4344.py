c=int(input())
output=[]
for i in range(c):
    n=list(map(int, input().split()))
    sum=0
    for j in range(1,n[0]+1):
        sum+=n[j]
    sum=sum/n[0]
    high=0
    for x in range(1,n[0]+1):
        if sum<n[x]:
            high+=1
    high=(high/n[0])*100
    output.append(high)
for i in range(c):
    print("%.3f%%" %output[i])