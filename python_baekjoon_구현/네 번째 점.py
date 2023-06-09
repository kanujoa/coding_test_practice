# 1번씩만 나온 수를 찾으면 된다. (적게 나온 수 찾기)

dots = []
diagonal = 0
x = {}
y = {}
answer_x = 0
answre_y = 0

for _ in range(3):
    a, b = map(int, input().split())
    dots.append([a, b])
for dot in dots:
    if dot[0] not in x:
        x[dot[0]] = 1
    else:
        x[dot[0]] += 1
    if dot[1] not in y:
        y[dot[1]] = 1
    else:
        y[dot[1]] += 1
for key in x:
    if x[key] == 1:
        answer_x = key
for key in y:
    if y[key] == 1:
        answer_y = key

print(answer_x, answer_y)