num=int(input())
for i in range(num):
    X=list(map(int,input().split()))
    A=X[0]+X[1]
    print("Case #{}: {}".format(i+1, A))