def solution(s):
    s = s.lower()     # 대소문자를 구별하지 않으므로 일단 다 소문자로 만들어줌.
    p_cnt = 0     # p(P)의 개수를 세는 p_cnt 만듦
    y_cnt = 0     # y(Y)의 개수를 세는 y_cnt 만듦
    for i in s:     # 문자열 s 안의 각 문자를 i라 함
        if i == "p":     # i가 p이면
            p_cnt += 1     # p_cnt 1 증가   
        elif i == "y":     # i가 y이면
            y_cnt += 1     # y_cnt 1 증가
    if p_cnt == y_cnt:     # p와 y의 개수를 다 센 후 p의 개수와 y의 개수를 비교하여 같으면(둘 다 존재하지 않을 때도 0개로 같은 것이므로 true 반환)
        return True     # true 반환
    else:     # 개수가 다르면
        return False     # false 반환