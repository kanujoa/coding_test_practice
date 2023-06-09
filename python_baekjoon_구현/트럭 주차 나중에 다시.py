a, b, c = map(int, input().split())     # 한 대 주차 시 1분에 A원, 두 대 주차 시 1분에 B원, 세 대 주차 시 1분에 C원
time = []

for _ in range(3):
    arrive, depart = map(int, input().split())
    time.append([arrive, depart])
time.sort()

time_ch = [0] * (time[-1][1] - time[0][0] + 2)
for i in time:
    for j in range(i[0], i[1]):
        time_ch[j] += 1
    time_ch[i[0]] -= 1

print(answer)