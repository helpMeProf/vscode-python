N=int(input())
M=int(input())
d=[[-1 for i in range(101)] for j in range(101)]
import math

def combination(n,m):
    if n==0 or m==0:
        return 1
    if d[n][m] != -1:
        return d[n][m]
    if n==m :
        d[n][m]=1
        return d[n][m]
    d[n][m]=(combination(n-1,m)+combination(n-1,m-1))
    return d[n][m]

a=combination(N,M)


sum = math.factorial(N)//math.factorial(N-M)//math.factorial(M)
 
print(str(sum))
print(str(d[N][M]))
print(str(a))