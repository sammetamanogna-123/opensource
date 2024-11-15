def r(s):
    if not s:
        return ""
    result=[]
    count=1
    length=len(s)
    for i in range(1,length):
        
        if s[i]==s[i-1]:
            count+=1
        else:
            result.append(s[i-1] + str(count))
            count=1
    result.append(s[-1]+str(count))
    return "".join(result)
a=input().strip()
b=r(a)
print(b)
    
