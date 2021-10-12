n,m,n0=map(int, input().split())
mat=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int, input().split())
    mat[a].append(b)
    mat[b].append(a)

#dfs
check=[False for _ in range(n+1)]
print(n0, end=" ")
check[n0]=True
for x in range(len(mat)-1):
    for i in range(len(mat[n0])):#3
        tmp=mat[n0][i]
        for j in range(len(mat[tmp])):
            if check[tmp]==False:
                print(tmp, end=" ")
                check[tmp]=True
