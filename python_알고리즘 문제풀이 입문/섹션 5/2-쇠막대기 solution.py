# 여는 괄호는 무조건 stack에다 append, 닫는 괄호를 만났을 때는 앞 순서의 괄호가 여는 괄호인지 확인 후 맞으면 그 여는 괄호를 stack에서 지워준다.
# pop한 후 stack의 길이는 레이저를 기준으로 왼쪽 조각들의 개수이므로 이것을 하나의 변수에 계속 누적한다.

s = input()
stack = []
cnt = 0
for i in range(len(s)):
    if s[i] == '(':     # 문자열의 index i의 값이 여는 괄호면
        stack.append(s[i])     # stack에 그 값을 추가한다.
    else:     # 문자열의 index i의 값이 닫는 괄호면
        stack.pop()      # stack을 pop시키고 (닫는 괄호일 경우 이전 괄호가 어떤 것이든 상관없이 pop 과정을 거쳐야 하기 때문에 이 코드를 작성해 주었다.)
        if s[i-1] == '(':     # 그 바로 이전 괄호가 여는 괄호이면 레이저가 되므로
            cnt += len(stack)     # cnt에 stack의 길이를 누적시킨다.
        else:     # index i의 값이 닫는 괄호면 쇠막대기의 끝이 된다는 의미! 
            cnt += 1     # cnt에 1을 추가한다. (끝나는 것에 해당하는 막대기의 마지막 조각을 의미)
print(cnt)