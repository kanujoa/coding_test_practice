# 빼기와 나누기의 경우 이전 요소에서 최근 요소를 빼거나 나누어야 함. 이 순서 기억!

a = input()      # string type
stack = []

for x in a:
    if x.isdecimal():
        stack.append(int(x))
    else:
        if x == '+':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 + n1)
        elif x == '-':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 - n1)
        elif x == "*":
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 * n1)
        elif x == "/":
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 / n1)
print(stack[0])