def solution(dartResult):
    dart = dartResult
    prev = []
    cur = 0
    for i in range(len(dart)):
        if dart[i].isdecimal():
            if dart[i-1] == "1":
                cur = 10
            else:
                prev.append(cur)
                cur = int(dart[i])
        elif dart[i] == "D":
            cur = cur ** 2
        elif dart[i] == "T":
            cur = cur ** 3
        elif dart[i] == "*":
            cur *= 2
            prev[-1] *= 2
        elif dart[i] == "#":
            cur *= -1
    return cur + sum(prev)

print(solution("1D2S3T*"))

# 다른 풀이
# def solution(dartResult):
#     point = []
#     answer = []
#     dartResult = dartResult.replace('10','k')
#     point = ['10' if i == 'k' else i for i in dartResult]
#     print(point)

#     i = -1
#     sdt = ['S', 'D', 'T']
#     for j in point:
#         if j in sdt :
#             answer[i] = answer[i] ** (sdt.index(j)+1)
#         elif j == '*':
#             answer[i] = answer[i] * 2
#             if i != 0 :
#                 answer[i - 1] = answer[i - 1] * 2
#         elif j == '#':
#             answer[i] = answer[i] * (-1)
#         else:
#             answer.append(int(j))
#             i += 1
#     return sum(answer)