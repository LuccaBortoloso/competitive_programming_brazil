t, m, n = map(int,input().split())
melhor = 2**(t-1)
#for i in range(0,n-m+1+1):
#    if i-t <= 0:   
mat = [[0]*(t*2+1)]*(t+1)
mat[0][t] = 1
for x in mat:
    print(x)
