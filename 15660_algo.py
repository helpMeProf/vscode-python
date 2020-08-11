N=int(input())
M=int(input())

a=[]

def func(next) :
    if len(a)==M:
        for i in range(1,M):
            print(str(a[i]),end=' ')
        print()
        return
    for  i in range(next,N+1):
        if M-len(a)<=N-i+1:
            a.append(i)
            func(i+1)
            a.pop(len(a)-1)

func(0)