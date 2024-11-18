n=int(input())
arr=list(map(int,input().split()))
sort=True
for i in range(n-1):
    if arr[i]>arr[i+1]:
        sort=False
        break
print("true" if sort else "false")
