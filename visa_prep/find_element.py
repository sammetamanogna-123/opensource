def binary_search(arr,x):
    l=0
    h=len(arr)-1
    while l<=h:
        m=(l+h)//2
        if arr[m]==x:
            return m
        elif arr[m]<x:
            l=m+1
        else:
            h=m-1
    return -1
n=int(input())
arr=list(map(int,input().split()))
x=int(input())
res=binary_search(arr,x)
print(res)
