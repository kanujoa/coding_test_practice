def solution(s):
    stack = []
    for x in s:
        if len(stack) == 0 or x == "(":
            stack.append(x)
        elif x == ")" and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(x)
    if len(stack) == 0:
        return True
    else:
        return False
    
print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))


# 깔끔한 풀이
def is_pair(s):
    wt = 0
    for c in s :
        if c == '(' : wt += 1     # '(' 일 경우에는 +1
        elif c == ')' : wt -= 1     # ')'일 경우에는 -1
        if wt < 0 : return False
    return wt == 0     # wt가 음수도 양수도 아닌 0이어야지 True가 됨

print(is_pair(")))((("))