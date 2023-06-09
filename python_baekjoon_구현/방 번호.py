# 6과 9는 하나의 인덱스에다가만 수를 증가시켜 하나로 처리하면 되는 간단한 문제....

number = input()

need = [0] * 9
for num in number:
    if num == '6' or num == '9':
        need[6] += 1
    else:
        need[int(num)] += 1
if need[6] % 2 == 0:
    need[6] //= 2
else:
    need[6] = need[6] // 2 + 1
print(max(need))

