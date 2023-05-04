# 이 문제에서 소문자를 밀어서 대문자를 만들 수는 없다.
# 소문자는 아무리 밀어도 소문자, 대문자도 아무리 밀어도 대문자임.

def solution(s, n):
    tmp = []
    for i in s:
        if i == ' ':
            tmp.append(' ')
        else:
            push = ord(i) + n
            if i.isupper():
                tmp.append(chr(65 + (push - 65) % 26))
            else:
                tmp.append(chr(97 + (push - 97) % 26))
    return ''.join(tmp)     