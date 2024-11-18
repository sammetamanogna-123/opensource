def m(n,arr):
    p,q=0,0
    for r in arr:
        if r==0:
            q+=1
        else:
            p=max(p,q)
            q=0
    return max(p,q)
n=int(input())
arr=list(map(int,input().split()))
print(m(n,arr))
