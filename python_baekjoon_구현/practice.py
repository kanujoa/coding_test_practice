l = [0] * 35
bind = 0
if len(l) % 20 == 0:
    bind = len(l) // 20
else:
    bind = len(l) // 20 + 1
for i in range(bind):
    print(' '.join(map(str, l[20*i : 20*(i+1)])))        