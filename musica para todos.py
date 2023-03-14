def troca(n,m,c,ami_ama,ami_od):
    if n > 0:
        nao_gosta = 0
        qtd = 0
        for x in range(1000000):
                for i in range(n):
                    if(c == ami_od):
                        nao_gosta = nao_gosta+1
                if (nao_gosta == 0 and ami_od == c):
                    c = ami_ama
                    qtd+=1
                elif(nao_gosta > 0 and ami_od == c):
                    c = ami_ama
                    qtd+=1
                if(qtd > 100000):
                    print('-1')
                else:
                    print(qtd)
                    break
                    
n,m,c = input().split(' ')
n = int(n)
m = int(m)
c = int(c)
for x in range(n):
    amigos_amam, amigos_odeiam = input().split(' ')
    amigos_amam = (int(amigos_amam))
    amigos_odeiam = (int(amigos_odeiam))
if( n >= 1 and n <=100000 and m>=1 and m <=100000 and c >=1 and c <=m):
    troca(n,m,c,amigos_amam,amigos_odeiam)
    