def solution(t, p):
    cnt = 0
    for i in range(len(t)-len(p)+1):
        num = ""
        for j in t[i: i+len(p)]:
            num += j
        if len(num) > 1 and num[0] == '0':
            num = num[1:]
        if int(num) <= int(p):
            cnt += 1
    return cnt

# print(solution("10203", "15"))
print(solution("500220839878", "7"))


# 좀 더 간단한 풀이
# def solution(t, p):
#     answer = 0

#     for i in range(len(t) - len(p) + 1):
#         if int(p) >= int(t[i:i+len(p)]):     --> 주목! 슬라이싱 한 부분을 그대로 int로 형변환만 해주면 숫자가 된다!
#             answer += 1

#     return answer