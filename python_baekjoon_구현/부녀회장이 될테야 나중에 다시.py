T = int(input())

for _ in range(T):
    k = int(input())     # k층
    n = int(input())     # n호
    live = 0
    for i in range(1, n+1):
      live += 1
    if k == 0:
        print(live)
    else:
        floor = 1
        while floor <= k:
            floor += 1
            live = live * n * n
        print(live)