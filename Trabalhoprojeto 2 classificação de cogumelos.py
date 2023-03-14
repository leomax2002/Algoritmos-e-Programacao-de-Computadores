def converte_cogumelo(carac):
    new_cogumelo = []
    conv = {
    0:{'b':0,'c':1,'x':2,'f':3,'k':4,'s':5},
    1:{'f':0,'g':1,'y':2,'s':3},
    2:{'n':0,'b':1,'c':2,'g':3,'r':4,'p':5,'u':6,'e':7,'w':8,'y':9},
    3:{'t':0,'f':1},
    4:{'a':0,'l':1,'c':2,'y':3,'f':4,'m':5,'n':6,'p':7,'s':8},
    5:{'a':0,'d':1,'f':2,'n':3},
    6:{'c':0,'w':1,'d':2},
    7:{'b':0,'n':1},
    8:{'k':0,'n':1,'b':2,'h':3,'g':4,'r':5,'o':6,'p':7,'u':8,'e':9,'w':10,'y':11},
    9:{'e':0,'t':1},
    10:{'b':0,'c':1,'u':2,'e':3,'z':4,'r':5,'?':6},
    11:{'f':0,'y':1,'k':2,'s':3},
    12:{'f':0,'y':1,'k':2,'s':3},
    13:{'n':0,'b':1,'c':2,'g':3,'o':4,'p':5,'e':6,'w':7,'y':8},
    14:{'n':0,'b':1,'c':2,'g':3,'o':4,'p':5,'e':6,'w':7,'y':8},
    15:{'p':0,'u':1},
    16:{'n':0,'o':1,'w':2,'y':3},
    17:{'n':0,'o':1,'t':2},
    18:{'c':0,'e':1,'f':2,'l':3,'n':4,'p':5,'s':6,'z':7},
    19:{'k':0,'n':1,'b':2,'h':3,'r':4,'o':5,'u':6,'w':7,'y':8},
    20:{'a':0,'c':1,'n':2,'s':3,'v':4,'y':5},
    21:{'g':0,'l':1,'m':2,'p':3,'u':4,'w':5,'d':6},
    }
    for x in range(len(carac)):
        new_cogumelo.append(conv[x][carac[x]])
    return new_cogumelo
#entradas    
k = int(input())
ntrain, ntest = [int(x) for x in input().split()]
#listinhas
grupo_cogumelos = []
classificacao_cogumelos = {}
grupo_cogumelos_teste = []
u = []
dp = []
gp_cogumelos_norm = []
gp_cogumelos_test_norm= []
distancia_cogumelos = []
#criando cogumelos
for i in range(ntrain):
    cogumelo = converte_cogumelo(input().split())
    grupo_cogumelos.append(cogumelo)
#medias dos atributos dos cogumelos
for i in range(22):
    m = 0
    for j in range(len(grupo_cogumelos)):
        m += grupo_cogumelos[j][i]
    u.append(m/ntrain)
#desvio padrão dos atributos dos cogumelos
for i in range(22):
    desv = 0
    for j in range(len(grupo_cogumelos)):
        desv+=(grupo_cogumelos[j][i]-u[i])**2
    dp.append((desv/ntrain)**(0.5))
#normalizando cogumelos
for i in grupo_cogumelos:
    grupo_norm = []
    for j in range(22):
        if dp[j] == 0:
            grupo_norm.append(0)
        else:
            grupo_norm.append((i[j]-u[j])/dp[j])
    gp_cogumelos_norm.append(grupo_norm)
#lendo a classificação
for i in range(ntrain):
    classificacao_cogumelos[i] = input()
#lendo novos cogumelos
for i in range(ntest):
    cogumelo = converte_cogumelo(input().split())
    grupo_cogumelos_teste.append(cogumelo)
#normalizando os novos cogumelos
for i in grupo_cogumelos_teste:
    grupo_norm = []
    for j in range(22):
        if dp[j] == 0:
            grupo_norm.append(0)
        else:
            grupo_norm.append((i[j]-u[j])/dp[j])
    gp_cogumelos_test_norm.append(grupo_norm)
#calculando a distancia entre cogumelos
for i in gp_cogumelos_test_norm:
    dist = 0
    dist_cog = []
    for j in gp_cogumelos_norm:
        dist = 0
        for z in range(22):
            dist += (i[z] - j[z])**2
        dist_cog.append(dist**(0.5))
    distancia_cogumelos.append(dist_cog)
#classificando cogumelos
for i in distancia_cogumelos:
    mais_proximos = []
    clas_cogumelo = i.copy()
    clas_cogumelo.sort()
    cont_p = 0
    cont_e = 0
    for j in range(k):
        mais_proximos.append(i.index(clas_cogumelo[j]))
    for z in mais_proximos:
        if(classificacao_cogumelos[z] == 'e'):
            cont_e+=1
        else:
            cont_p+=1
    if(cont_e > cont_p):
        print('e')
    else:
        print('p')