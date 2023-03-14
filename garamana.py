def anagrama(p,a,n,tam):
    for x in range(len(p)):
        for i in range(len(a)):
            if(p[x] == a[i] or a[i] == '*'):
                n = n+1
                break
    if (n == tam):
        print('S')
    else:
        print('N')
p = input()
a = input()
n = 0
tam = len(p)
ver = 0
if(tam >=1 and tam<=100 and len(a) == len(p)):
    for x in range (len(p)):
        if(p[x] == 'a' or p[x] == 'b' or p[x] == 'c' or p[x] == 'd' or p[x] == 'e' or p[x] == 'f' or p[x] == 'g' or p[x] == 'h' or p[x] == 'i' or p[x] == 'j' or p[x] == 'k' or p[x] == 'l' or p[x] == 'm' or p[x] == 'n' or p[x] == 'o' or p[x] == 'p' or p[x] == 'q' or p[x] == 'r' or p[x] == 's' or p[x] == 't' or p[x] == 'u' or p[x] == 'v' or p[x] == 'w' or p[x] == 'x' or p[x] == 'y' or p[x] == 'z'):
            ver = ver+1
        if(a[x] == 'a' or a[x] == 'b' or a[x] == 'c' or a[x] == 'd' or a[x] == 'e' or a[x] == 'f' or a[x] == 'g' or a[x] == 'h' or a[x] == 'i' or a[x] == 'j' or a[x] == 'k' or a[x] == 'l' or a[x] == 'm' or a[x] == 'n' or a[x] == 'o' or a[x] == 'p' or a[x] == 'q' or a[x] == 'r' or a[x] == 's' or a[x] == 't' or a[x] == 'u' or a[x] == 'v' or a[x] == 'w' or a[x] == 'x' or a[x] == 'y' or a[x] == 'z' or a[x] == '*'):
            ver = ver+1
if(ver == 2*tam):
    anagrama(p,a,n,tam)