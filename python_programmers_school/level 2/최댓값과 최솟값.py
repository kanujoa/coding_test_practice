def solution(s):
    s = list(map(int, s.split()))
    return ' '.join([str(min(s)), str(max(s))])


# 살짝 다른 풀이
def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))     # join이 아닌 + 연산자를 사용하여 공백으로 연결해 주었다.
