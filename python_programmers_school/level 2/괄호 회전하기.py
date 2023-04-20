from collections import deque

def solution(s):
    result = 0
    stack = []
    rule = {')': '(', ']': '[', '}': '{'}
    deq = deque(s)
    while True:     # python에서 do ~ while ...은 while True로 실현시킬 수 있다.
        for x in deq:
            if x == '[' or x == '(' or x == '{'or len(stack) == 0:
                stack.append(x)
            else:
                if stack[-1] == rule[x]:
                    stack.pop()
                else:
                    stack.append(x)
        if len(stack) == 0:
            result += 1
        deq.append(deq.popleft())
        stack.clear()
        if ''.join(list(deq)) == s:
            break
    return result 

print(solution("}]()[{"))
print(solution("[](){}"))

# 다른 사람의 풀이
def is_valid(s):     # 조건을 여러개로 나누어서 stack 채우기
    stack = []
    for ch in s:
        if not stack:     # stack 리스트에 해당 요소(ch)가 없음을 나타냄.
            stack.append(ch)
        elif stack[-1] == '(':
            if ch==')': stack.pop()
            else: stack.append(ch)
        elif stack[-1] == '{':
            if ch=='}': stack.pop()
            else: stack.append(ch)
        elif stack[-1] == '[':
            if ch==']': stack.pop()
            else: stack.append(ch)

    return False if stack else True     # stack에 요소가 남아 있는 상태라면 False, 빈 상태라면 True 반환

def solution(s):
    answer = 0
    for i in range(len(s)):
        answer += is_valid(s[i:]+s[:i])     # 문자열 슬라이싱과 + 연산자로 문자열을 재조합하여 왼쪽으로 요소를 옮기는 효과를 냄.
    # 여기에서 반환값이 True일 경우 1이 answer에 더해지게 되고, False인 경우 0이 더해지게 됨.
    return answer

print(solution("}]()[{"))