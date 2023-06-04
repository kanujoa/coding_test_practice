number = map(int, input().split())

_sum = 0
for n in number:
    _sum += n ** 2
print(_sum % 10)