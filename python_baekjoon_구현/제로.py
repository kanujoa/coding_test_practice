k = int(input())
stack = []

for _ in range(k):
    num = int(input())
    if num == 0:
        if len(stack) != 0:
            stack.pop()
    else:
        stack.append(num)
if len(stack) == 0:
    print(0)
else:
    print(sum(stack))