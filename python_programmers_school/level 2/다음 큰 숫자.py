def solution(n):
    one_cnt = bin(n).count('1')
    current = n     # current를 따로 설정해 주지 않고 아래에서 n += 1로 한번에 작성하면 코드의 길이가 줄어든다.
    while True:
        current += 1    
        if bin(current).count('1') == one_cnt:
            return current