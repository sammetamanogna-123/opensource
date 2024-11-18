t=int(input())
result=[]
for _ in range(t):
    x,n=map(int,input().split())
    points=x//10
    s=points*n
    result.append(s)
for r in result:
    print(r)
