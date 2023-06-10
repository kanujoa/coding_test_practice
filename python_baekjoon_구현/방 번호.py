number = input()

need = {}
for num in number:
    if num not in need:
        need[num] = 1
    else:
        need[num] += 1
if '6' in need and '9' not in need:
    if need['6'] % 2 == 0:
        need['6'] //= 2
    else:
        need['6']  = need['6'] // 2 + 1
elif '9' in need and '6' not in need:
    if need['9'] % 2 == 0:
        need['9'] //= 2
    else:
        need['9']  = need['9'] // 2 + 1
print(max(need.values()))
