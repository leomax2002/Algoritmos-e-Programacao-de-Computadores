def menos_gelo(blocos,n,m):
    if(m%blocos[n-1] == 0):
        return int(m/blocos[n-1])
    resp = [999999]*1000002
    resp[0] = 0
    for i in range(n):
        k = blocos[i]
        j = k
        while j <= m:
            resp[j] = min(resp[j],resp[j-k]+1)
            j+=1
    return int(resp[m])
def num_gelo(blocos,n,m):
    num = 0
    n = n - 1
    while m > 0:
        while m < blocos[n]:
            n-=1
        m-= blocos[n]
        num+=1
    return num
inst = int(input())
for i in range(inst):
    n, m = [int(x) for x in input().split()]
    blocos = [int(x) for x in input().split()]
    blocos.sort()
    print(menos_gelo(blocos,n,m))