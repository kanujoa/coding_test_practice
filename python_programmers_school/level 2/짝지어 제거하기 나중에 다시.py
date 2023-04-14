def solution(s):
    while True:
        length = len(s)
        prev = ''
        for i in range(len(s)):
            if s[i] == prev:
                s = s.replace(s[i], '', 2)
                break
            else:
                prev = s[i]
        if len(s) == 0:
            return 1
        elif len(s) == length:
            return 0
        
        
print(solution("baabaa"))
print(solution("cdcd"))