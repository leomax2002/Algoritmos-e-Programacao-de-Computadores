from datetime import date
def trabalho1(N):
    cont_dentro,cont_fora = conta_alunos1(N)
    res1 = (cont_dentro/(cont_dentro+cont_fora))*100
    res2 = (cont_fora/(cont_dentro+cont_fora))*100
    print(f'matriculados ou formados:{res1:5.1f}')
    print(f'alunos em outras situacoes:{res2:5.1f}')
    
    
def trabalho2(N):
    cont_f, cont_m = conta_alunos2(N)
    res1 = (cont_m/(cont_m+cont_f))*100
    res2 = (cont_f/(cont_m+cont_f))*100
    print(f'sexo masculino:{res1:5.1f}')
    print(f'sexo feminino:{res2:5.1f}')
    
    
def trabalho3(N):
    cont_anos = conta_alunos3(N)
    res1 = (cont_anos)/N
    print(f'media de anos desde ingresso:{res1:5.1f}')
    
    
def trabalho4(N):
    cont_seg,cont_ter,cont_quart,cont_quint,cont_sext,cont_sab,cont_dom = conta_alunos4(N)
    res_seg = (cont_seg/N)*100
    res_ter = (cont_ter/N)*100
    res_quart = (cont_quart/N)*100
    res_quint = (cont_quint/N)*100
    res_sext = (cont_sext/N)*100
    res_sab = (cont_sab/N)*100
    res_dom = (cont_dom/N)*100
    print(f'domingo:{res_dom:5.1f}')
    print(f'segunda:{res_seg:5.1f}')
    print(f'terca:{res_ter:5.1f}')
    print(f'quarta:{res_quart:5.1f}')
    print(f'quinta:{res_quint:5.1f}')
    print(f'sexta:{res_sext:5.1f}')
    print(f'sabado:{res_sab:5.1f}')
    
def trabalho5(N):
    cont_dentro_m,cont_fora_m,cont_dentro_f,cont_fora_f = conta_alunos5(N)
    res1_m = (cont_dentro_m/(cont_dentro_m+cont_fora_m))*100
    res2_m = (cont_fora_m/(cont_dentro_m+cont_fora_m))*100
    
    res1_f = (cont_dentro_f/(cont_dentro_f+cont_fora_f))*100
    res2_f = (cont_fora_f/(cont_dentro_f+cont_fora_f))*100
    
    print(f'dentre masculinos:')
    print(f'matriculados ou formados:{res1_m:5.1f}')
    print(f'alunos em outras situacoes:{res2_m:5.1f}')
    print(f'dentre femininos:')
    print(f'matriculados ou formados:{res1_f:5.1f}')
    print(f'alunos em outras situacoes:{res2_f:5.1f}')
def trabalho6(N):
    cont_dentro_anos,cont_fora_anos, cont_dentro,cont_fora = conta_alunos6(N)
    res_dentro_1 = (cont_dentro_anos/cont_dentro)
    res_fora_2 = (cont_fora_anos/cont_fora)
    print(f'dentre matriculados ou formados:')
    print(f'media de anos desde ingresso:{res_dentro_1:5.1f}')
    print(f'dentre alunos em outras situacoes:')
    print(f'media de anos desde ingresso:{res_fora_2:5.1f}')
    
    
def trabalho7(N):
    cont_seg_f,cont_ter_f,cont_quart_f,cont_quint_f,cont_sext_f,cont_sab_f,cont_dom_f,cont_seg_m,cont_ter_m,cont_quart_m,cont_quint_m,cont_sext_m,cont_sab_m,cont_dom_m = conta_alunos7(N)
    res_seg_f = (cont_seg_f/(cont_seg_f+cont_ter_f+cont_quart_f+cont_quint_f+cont_sext_f+cont_sab_f+cont_dom_f))*100
    res_ter_f = (cont_ter_f/(cont_seg_f+cont_ter_f+cont_quart_f+cont_quint_f+cont_sext_f+cont_sab_f+cont_dom_f))*100
    res_quart_f = (cont_quart_f/(cont_seg_f+cont_ter_f+cont_quart_f+cont_quint_f+cont_sext_f+cont_sab_f+cont_dom_f))*100
    res_quint_f = (cont_quint_f/(cont_seg_f+cont_ter_f+cont_quart_f+cont_quint_f+cont_sext_f+cont_sab_f+cont_dom_f))*100
    res_sext_f = (cont_sext_f/(cont_seg_f+cont_ter_f+cont_quart_f+cont_quint_f+cont_sext_f+cont_sab_f+cont_dom_f))*100
    res_sab_f = (cont_sab_f/(cont_seg_f+cont_ter_f+cont_quart_f+cont_quint_f+cont_sext_f+cont_sab_f+cont_dom_f))*100
    res_dom_f = (cont_dom_f/(cont_seg_f+cont_ter_f+cont_quart_f+cont_quint_f+cont_sext_f+cont_sab_f+cont_dom_f))*100
    
    res_seg_m = (cont_seg_m/(cont_seg_m+cont_ter_m+cont_quart_m+cont_quint_m+cont_sext_m+cont_sab_m+cont_dom_m))*100
    res_ter_m = (cont_ter_m/(cont_seg_m+cont_ter_m+cont_quart_m+cont_quint_m+cont_sext_m+cont_sab_m+cont_dom_m))*100
    res_quart_m = (cont_quart_m/(cont_seg_m+cont_ter_m+cont_quart_m+cont_quint_m+cont_sext_m+cont_sab_m+cont_dom_m))*100
    res_quint_m = (cont_quint_m/(cont_seg_m+cont_ter_m+cont_quart_m+cont_quint_m+cont_sext_m+cont_sab_m+cont_dom_m))*100
    res_sext_m = (cont_sext_m/(cont_seg_m+cont_ter_m+cont_quart_m+cont_quint_m+cont_sext_m+cont_sab_m+cont_dom_m))*100
    res_sab_m = (cont_sab_m/(cont_seg_m+cont_ter_m+cont_quart_m+cont_quint_m+cont_sext_m+cont_sab_m+cont_dom_m))*100
    res_dom_m = (cont_dom_m/(cont_seg_m+cont_ter_m+cont_quart_m+cont_quint_m+cont_sext_m+cont_sab_m+cont_dom_m))*100
    
    print(f'dentre masculinos:')
    print(f'domingo:{res_dom_m:5.1f}')
    print(f'segunda:{res_seg_m:5.1f}')
    print(f'terca:{res_ter_m:5.1f}')
    print(f'quarta:{res_quart_m:5.1f}')
    print(f'quinta:{res_quint_m:5.1f}')
    print(f'sexta:{res_sext_m:5.1f}')
    print(f'sabado:{res_sab_m:5.1f}')
    
    print(f'dentre femininos:')
    print(f'domingo:{res_dom_f:5.1f}')
    print(f'segunda:{res_seg_f:5.1f}')
    print(f'terca:{res_ter_f:5.1f}')
    print(f'quarta:{res_quart_f:5.1f}')
    print(f'quinta:{res_quint_f:5.1f}')
    print(f'sexta:{res_sext_f:5.1f}')
    print(f'sabado:{res_sab_f:5.1f}')


def conta_alunos1(N):
    p = 0
    cont_dentro = 0
    cont_fora = 0
    while (p < N):
        a1,a2,a3,a4,a5,a6=[int(x) for x in input().split()]
        if(a6 == 2 or a6 == 6):
            cont_dentro= cont_dentro + 1
        else:
            cont_fora = cont_fora + 1
        p+=1
    return cont_dentro,cont_fora
            
            
def conta_alunos2(N):
    p = 0
    cont_f = 0
    cont_m = 0
    while (p < N):
        a1,a2,a3,a4,a5,a6=[int(x) for x in input().split()]
        if(a5 == 1):
            cont_f = cont_f + 1
        else:
            cont_m = cont_m + 1
        p+=1
    return cont_f,cont_m
               
def conta_alunos3(N):
    p = 0
    cont_anos = 0
    while (p < N):
        a1,a2,a3,a4,a5,a6=[int(x) for x in input().split()]
        cont_anos = cont_anos + (2019 - a1)
        p+=1
    return cont_anos
        
        
def conta_alunos4(N):
    p = 0
    cont_seg = 0
    cont_ter = 0
    cont_quart = 0
    cont_quint = 0
    cont_sext = 0
    cont_sab = 0
    cont_dom = 0
    while (p < N):
        a1,a2,a3,a4,a5,a6=[int(x) for x in input().split()]
        data = date(year = a4, month = a3, day = a2)
        dia_semana = data.weekday()
        if(dia_semana == 0):
            cont_seg+=1
        elif(dia_semana == 1):
            cont_ter+=1
        elif(dia_semana == 2):
            cont_quart+=1
        elif(dia_semana == 3):
            cont_quint+=1
        elif(dia_semana == 4):
            cont_sext+=1
        elif(dia_semana == 5):
            cont_sab+=1
        elif(dia_semana == 6):
            cont_dom+=1 
        p+=1
    return(cont_seg,cont_ter,cont_quart,cont_quint,cont_sext,cont_sab,cont_dom)
        
        
def conta_alunos5(N):
    p = 0
    cont_dentro_m = 0
    cont_fora_m = 0
    
    cont_dentro_f = 0
    cont_fora_f = 0
    while (p < N):
        a1,a2,a3,a4,a5,a6=[int(x) for x in input().split()]
        if((a6 == 2 or a6 == 6) and (a5 == 1)):
            cont_dentro_f+=1
        elif((a6 != 2 or a6 != 6) and (a5 == 1)):
            cont_fora_f+=1
        elif((a6 == 2 or a6 == 6) and (a5 == 2)):
            cont_dentro_m+=1
        elif((a6 != 2 or a6 != 6) and (a5 == 2)):
            cont_fora_m+=1
        p+=1
    return(cont_dentro_m,cont_fora_m,cont_dentro_f,cont_fora_f)
        
        
def conta_alunos6(N):
    p = 0
    cont_dentro_anos = 0
    cont_fora_anos = 0
    cont_dentro = 0
    cont_fora = 0
    while (p < N):
        a1,a2,a3,a4,a5,a6=[int(x) for x in input().split()]
        if(a6 == 2 or a6 == 6):
            cont_dentro_anos= cont_dentro_anos + (2019 - a1)
            cont_dentro+=1
        else:
            cont_fora_anos = cont_fora_anos + (2019 - a1)
            cont_fora+=1
        p+=1
    return cont_dentro_anos,cont_fora_anos,cont_dentro,cont_fora
        
        
def conta_alunos7(N):
    
    p = 0
    cont_m = 0
    cont_f = 0
    cont_seg_f = 0
    cont_ter_f = 0
    cont_quart_f = 0
    cont_quint_f = 0
    cont_sext_f = 0
    cont_sab_f = 0
    cont_dom_f = 0
    
    cont_seg_m = 0
    cont_ter_m = 0
    cont_quart_m = 0
    cont_quint_m = 0
    cont_sext_m = 0
    cont_sab_m = 0
    cont_dom_m = 0
    while (p < N):
        a1,a2,a3,a4,a5,a6=[int(x) for x in input().split()]
        data = date(year = a4, month = a3, day = a2)
        dia_semana = data.weekday()
        if(dia_semana == 0 and a5 == 1):
            cont_seg_f+=1
        elif(dia_semana == 1 and a5 == 1):
            cont_ter_f+=1
        elif(dia_semana == 2 and a5 == 1):
            cont_quart_f+=1
        elif(dia_semana == 3 and a5 == 1):
            cont_quint_f+=1
        elif(dia_semana == 4 and a5 == 1):
            cont_sext_f+=1
        elif(dia_semana == 5 and a5 == 1):
            cont_sab_f+=1
        elif(dia_semana == 6 and a5 == 1):
            cont_dom_f+=1
            
        elif(dia_semana == 0 and a5 == 2):
            cont_seg_m+=1
        elif(dia_semana == 1 and a5 == 2):
            cont_ter_m+=1
        elif(dia_semana == 2 and a5 == 2):
            cont_quart_m+=1
        elif(dia_semana == 3 and a5 == 2):
            cont_quint_m+=1
        elif(dia_semana == 4 and a5 == 2):
            cont_sext_m+=1
        elif(dia_semana == 5 and a5 == 2):
            cont_sab_m+=1
        elif(dia_semana == 6 and a5 == 2):
            cont_dom_m+=1 
        p+=1
    return(cont_seg_f,cont_ter_f,cont_quart_f,cont_quint_f,cont_sext_f,cont_sab_f,cont_dom_f,cont_seg_m,cont_ter_m,cont_quart_m,cont_quint_m,cont_sext_m,cont_sab_m,cont_dom_m)
               
T = int(input())
N = int(input())
if(T == 1):
    trabalho1(N)
elif(T == 2):
    trabalho2(N)
elif(T == 3):
    trabalho3(N)
elif(T == 4):
    trabalho4(N)
elif(T == 5):
    trabalho5(N)
elif(T == 6):
    trabalho6(N)
elif(T == 7):
    trabalho7(N)