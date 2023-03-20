def solution(strings, n):
    for i in range(len(strings)):     # 여기서 for i in strings 하고 i = i[n] + i 이렇게 한다면 원하는 대로 변경되지 않음.
        strings[i] = strings[i][n] + strings[i]     # strings[i] 이렇게 인덱스를 적어주어야 변경됨.
    strings.sort()
    for j in range(len(strings)):
        strings[j] = strings[j].replace(strings[j][0], "", 1)
    return strings

# 간단한 풀이
# def strange_sort(strings, n):
#     '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''
#     return sorted(sorted(strings), key=lambda x: x[n])     --> string 리스트 요소의 n번째 인덱스 기준으로 정렬하라는 의미  
# string에서 sort를 해주지 않으면 ["abce", "abcd", "cdx"], 2 같은 경우가 통과가 안됨.
# 2번째 index 기준으로 정렬하면 그대로이지만 문제에서 같은 문자열이 여러 개 나오면 사전순으로 정렬하라고 했음.