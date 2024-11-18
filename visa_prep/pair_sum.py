n=int(input().strip())
arr=list(map(int,input().split()))
k=int(input().strip())

flag=False
for i in range(n):
    for j in range(i+1,n):
        if arr[i]+arr[j]==k:
            
            flag=True
            break
    if flag:
        break
print("true" if flag else "false")
