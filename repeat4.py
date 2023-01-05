X=int(input())
N=int(input())
sum=0
for j in range(N):
    A=list(map(int,input().split()))
    mul=A[0]*A[1]
    sum+=mul
if (sum==X):
    print("Yes")
else:
    print("No")
