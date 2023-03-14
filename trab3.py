with open(input()) as arquivo:
    imagem = arquivo.read()
    magic_number = imagem[0]+imagem[1]
    tmp = ''
    resultado = 0
    if(magic_number == 'P1'):
        y = 0
        x = 2
        while x < len(imagem):
            if imagem[x] == '#':
                dif = (imagem.find('\n',x)- x)+1
                x+= dif
            if imagem[x].isdigit() and y < 2:
                tmp+=imagem[x]
            elif y <= 2:
                if tmp != '':
                    y+=1
            if y > 2:
                if(imagem[x] == '1'):
                    resultado+=1
            x+=1
    else:
        i = 2
        y = 0
        cont = 0
        soma = 0
        while i < len(imagem):
            if imagem[i] == '#':
                dif = (imagem.find('\n',i)- i)+1
                i+= dif
            elif imagem[i].isdigit():
                tmp+= imagem[i]
                i+=1
            else:
                if(tmp!= '' and y < 3):
                    if y == 2:
                        max_val = int(tmp)
                    tmp = ''
                    y+=1
                elif(tmp!= '' and y == 3):
                    if(magic_number == 'P3'):
                        cont+=1
                        soma+= int(tmp)
                        tmp = ''
                        if(cont == 3):
                            cont = 0
                            if(soma/3 > max_val/2):
                                resultado+=1
                            soma = 0
                    else:
                        data = int(tmp)
                        tmp = ''
                        if data > max_val/2:
                             resultado+=1
                i+=1
print(resultado)