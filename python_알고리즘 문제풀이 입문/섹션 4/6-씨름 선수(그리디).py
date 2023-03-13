n = int(input())
players = []
for _ in range(n):
    players.append(list(map(int, input().split())))
players.sort(reverse=True)
cnt = 1
for i in range(n):
    if i > 0:
        for x in range(i):
            if players[x][1] > players[i][1]:
                break
        else:
            cnt += 1
print(cnt)