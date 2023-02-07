def solution(s):
    result = ""
    for i in s:
        if s.count(i) == 1:
            result += i
    return "".join(sorted(result))

print(solution("abcabcadc"))

# 간단한 풀이
# def solution(s):
#     answer = "".join(sorted([ ch for ch in s if s.count(ch) == 1]))      --> 1번만 등장한 문자 리스트에 넣고 오름차순 정렬한 후에 합치기
#     return answer