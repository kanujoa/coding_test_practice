max = 0
i = 1
for _ in range(9):
    num = int(input())
    if num > max:
        max = num
    i += 1
print(max)
print(i)