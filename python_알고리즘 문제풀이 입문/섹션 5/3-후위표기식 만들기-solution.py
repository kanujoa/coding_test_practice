# stack에 있는 부호가 현재 들어갈 부호보다 우선순위가 높거나 같으면 stack에 있는 부호를 먼저 연산처리(pop)해야 한다. (stack에 들어 있는 모든 부호를 살펴봐야 한다.)
# 즉, 자기와 우선순위가 같거나 자기보다 높은 것들만 꺼내주어야 한다.
# stack에 있는 부호가 우선순위가 높지 않은 경우 그냥 새로운 부호 append
# 여는 괄호는 닫는 괄호를 만났을 때 꺼내야 한다. (둘이 쌍이므로)
# 여는 괄호 뒤에 온 부호들은 위와 같은 방식으로 닫는 괄호가 나타날 때까지 바로바로 연산처리 해 주어야 함.
# 괄호 모두 처리 후 stack에 있는 부호들은 후입선출의 방식으로 꺼내줌.

a = input()
stack = []
res = ''
for x in a:
    if x.isdecimal():     # x가 10진수 숫자인지 확인
        res += x
    else:
        if x == '(':     # 여는 괄호일 경우
            stack.append(x)     # 무조건 append
        elif x == '*' or x == '/':     # *나 /인 경우
            while stack and (stack[-1] == "*" or stack[-1] == "/"):     # stack이 비어 있지 않고 stack의 맨 끝 부호가 우선순위가 같은 *이나 /인 경우
                res += stack.pop()     # res에 stack의 마지막 요소를 누적 (*나 /가 나오지 않을 때까지 반복)
            stack.append(x)     # pop후 본인 append
        elif x == '+' or x == '-':     # +나 -인 경우 모든 부호의 우선순위가 자신과 같거나 높다.   
            while stack and stack[-1] != '(':     # stack이 비어 있지 않고 stack의 마지막 요소가 여는 괄호가 아닐 때 동안 반복
                res += stack.pop()     # stack의 마지막 요소를 pop 후 res에 누적 (반복)
            stack.append(x)     # 마지막에 자신을 stack에 추가
        elif x == ')':      # 닫는 괄호일 경우
            while stack and stack[-1] != '(':     # stack이 비어 있지 않고 stack의 마지막 요소가 여는 괄호가 아닐 때 동안 반복
                res += stack.pop()     # stack의 마지막 요소를 꺼내서 res에 누적 (반복)
            stack.pop()     # 여는 괄호는 출력하지 않고 꺼내 주어야 한다.
while stack:     # 위의 것을 다 했음에도 stack이 비어 있지 않을 수 있기 때문에 stack이 비어 있지 않을 동안 아래의 실행문을 실행해준다.
    res += stack.pop()
print(res)