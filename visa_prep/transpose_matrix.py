n=int(input())
mat=[]
for _ in range(n):
    r=list(map(int,input().split()))
    mat.append(r)
trans=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        trans[i][j]=mat[j][i]
for r in trans:
    print(*r)
