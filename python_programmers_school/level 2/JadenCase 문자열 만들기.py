# 공백이 여러 개 존재할 수 있다고 했으므로 하나하나씩 살폈다.

def solution(s):
    result = ''
    prv = ''
    for i in range(len(s)):
        if prv == ' ' or i == 0:
            if s[i].isdigit() == False:
                result += s[i].upper()
                prv = s[i].upper()
            else:
                result += str(s[i])
                prv = str(s[i])
        else:
            result += s[i].lower()
            prv = s[i].lower()
    return result   
    
# print(solution("for the last week"))
print(solution("3people unFollowed me"))