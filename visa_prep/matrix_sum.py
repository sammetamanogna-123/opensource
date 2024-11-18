def sum_matrix(n,matrix):
    row=[0]*n
    col=[0]*n
    for i in range(n):
        row[i]=sum(matrix[i])
    
    for j in range(n):
        col[j]=sum(matrix[i][j] for i in range(n))
        
    res=[row[i]+col[i] for i in range(n)]
    print(" ".join(map(str,res)))
n=int(input())
matrix=[list(map(int,input().split())) for _ in range(n)]
sum_matrix(n,matrix)
