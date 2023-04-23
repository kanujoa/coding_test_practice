def solution(s):
    while s != '':
        s = [letter for letter in s]
        prv = ''
        for i in range(len(s)):
            if s[i] == prv:
                s[i] = ''
                s[i-1] = ''
            else:
                prv = s[i]
        if '' not in s:
            break
        s = ''.join(s)
    if len(s) == 0:
        return 1
    return 0    
        
        
print(solution("baabaa"))
print(solution("cdcd"))