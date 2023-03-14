def check(s,n):
    j = 0
    for i in range(n):
        if s[i] == s[n-i-1]:
            continue
        else:
            print('NO')
            j = 1
            break
    if j == 0:
        print(s)
def solution(s):
    new_s = ''
    n = len(s)
    for i in range(n):
        if(s[i] !='?'):
                new_s+=s[i]
        else:
            if i <=n//2:
                if s[n-i-1] != '?':
                    new_s+=s[n-i-1]
                else:
                    new_s+='a'
            else:
                new_s+='a'
    check(new_s,n)
        
    
        
solution('r?d?r')
#?ab??a
#bab??a
#?a?