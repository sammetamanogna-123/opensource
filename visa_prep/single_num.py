n=int(input())
arr=list(map(int,input().split()))
res=0
for num in arr:
    res ^= num
print(res)
