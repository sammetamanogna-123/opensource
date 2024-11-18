n=int(input())
matrix=[]
for _ in range(n):
    row=list(map(int,input().split()))
    matrix.append(row)
    
for i in range(n):
    print(*matrix[i][::-1])
