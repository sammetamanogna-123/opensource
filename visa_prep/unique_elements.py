def elements():
    n=int(input())
    arr=list(map(int,input().split()))
    s=set()
    result=[]
    for num in arr:
        if num not in s:
            result.append(num)
            s.add(num)
    print(" ".join(map(str,result)))
elements()
