x,n=map(int,input().split())
exist_capacity=x*100
rqd_planes=(n+99)//100
new_planes=max(0,rqd_planes-x)
print(new_planes)
