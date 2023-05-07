# stack을 사용한 풀이
def solution(s):
    stack = []
    for letter in s:
        if len(stack) == 0:
            stack.append(letter)
        elif stack[-1] == letter:
            stack.pop()
        else:
            stack.append(letter)
    return 1 if len(stack) == 0 else 0

# 일부 테스트 케이스 실패, 하나는 시간 초과 (위의 코드와 같이 아예 접근 방식을 바꾸어야 함!)
# from collections import Counter

# def solution(s):
#     letter_cnt = Counter(s)
#     while len(s) != 0:
#         for letter in reversed(letter_cnt):
#             s = s.replace(letter+letter, '')
#             if len(s) == sum(letter_cnt.values()):
#                 return 0
#             else:
#                 letter_cnt[letter] -= sum(letter_cnt.values()) - len(s)
#     return 1

# # print(solution('baabaa'))
# print(solution('cdcd'))


# # 효율성 테스트에서 실패
# def solution(s):
#     s = list(s)
#     idx = 1
#     if len(s) == 0 or len(s) == 1:
#         return 0
#     while len(s) != 0:
#         if s[idx] == s[idx - 1]:
#             s.pop(idx)
#             s.pop(idx - 1)
#             if idx != 1:
#                 idx -= 1
#         else:
#             idx += 1
#         if idx == len(s):
#             return 0
#     return 1

# print(solution('baabaa'))
# print(solution('cdcd'))
# print(solution('a'))
# print(solution('aaaaa'))