import numpy as np

def www(a,b,c):
    w=np.ones([a+1,b+1,c+1])
    for x in range(1,a+1):
        for y in range(1,b+1):
            for z in range(1,c+1):
                if x>20 or y>20 or z>20:
                    w[x][y][z]=w[20][20][20]
                elif x<y and y<z:
                    w[x][y][z]=w[x][y][z-1]+w[x][y-1][z-1]-w[x][y-1][z]
                else:
                    w[x][y][z]=w[x-1][y][z]+w[x-1][y-1][z]+w[x-1][y][z-1]-w[x-1][y-1][z-1]
    return w[a][b][c]

while True:
    num=[]
    a,b,c=map(int,input().split())
    if a==-1 and b==-1 and c==-1:
        break
    num.append([a,b,c,www(a,b,c)])
for i in range(len(num)):
    print("w(%d, %d, %d) = %d" %(num[i][0],num[i][1],num[i][2],num[i][3]))