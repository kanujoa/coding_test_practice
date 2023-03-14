def solution(s):
    sort = sorted([ord(i) for i in s], reverse=True)      # 큰 것부터 작은 것까지 문자를 정렬해야 함. 따라서 reverse와 ord 사용
    result = ""
    for x in sort:
        result += chr(x)
    return result

# 간단한 풀이
# def solution(s):
#     return ''.join(sorted(s, reverse=True))     --> 파이썬에서는 sorted를 사용하면 문자열도 크기 순서대로 자동 정렬된다.