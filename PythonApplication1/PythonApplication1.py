N=int(input())
res=[]
for i in range(1<=N<=100000):
    a=list(map(int,input().split()))
    print(a)
    a.insert(0,a[-1])
    a.pop(-1)
    print(a)

