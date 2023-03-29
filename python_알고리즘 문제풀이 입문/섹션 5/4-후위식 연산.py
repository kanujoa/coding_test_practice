# 헷갈리게 변수 여러개 만들지 말고 아래처럼 하나의 stack 안에서 처리해야지 오류가 없다.
expression = input()
stack = []

for i in expression:
    if i.isdecimal():
        stack.append(int(i))
    else:
        if i == "+":
            stack.append(stack.pop() + stack.pop())
        elif i == "*":
            stack.append(stack.pop() * stack.pop())
        elif i == "-":
            stack.append(stack.pop(-2) - stack.pop())
        elif i == "/":
            stack.append(stack.pop(-2) / stack.pop())
print(stack[0])