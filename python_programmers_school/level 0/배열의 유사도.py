def solution(s1, s2):
    result = 0
    for i in s1:
        if i in s2:
            result += 1
    return result

# 간단한 풀이
# def solution(s1, s2):
#     return len(set(s1)&set(s2))     --> s1과 s2를 집합 자료형으로 바꾼 뒤 교집합을 구해 그것의 개수를 len을 통해 구하는 코드이다.