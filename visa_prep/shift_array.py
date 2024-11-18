n=int(input())
arr=list(map(int,input().split()))
k=int(input())
k=k%n
rotate_arr=arr[-k:] + arr[:-k] if k != 0 else arr
print(*rotate_arr)
