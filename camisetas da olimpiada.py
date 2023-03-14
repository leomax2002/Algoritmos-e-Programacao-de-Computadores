#variáveis
n = int(input())
t1 = input().split(' ')
p = int(input())
m = int(input())
#variáveis auxiliares
np = 0
nm = 0
#pegando a quantidade produzida de tamanho pequeno e médio
if(n >=1 and n <=1000 and p>=0 and p<=1000 and m>=0 and m<=1000 and n <= p+m):
    for x in range(len(t1)):
        if(t1[x] == '1'):
            np+=1
        if (t1[x] == '2'):
            nm+=1
#resultados
    if(p == np and m == nm and n <= (np+nm)):
        print('S')
    else:
        print('N')