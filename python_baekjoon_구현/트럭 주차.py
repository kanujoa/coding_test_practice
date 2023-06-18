a, b, c = map(int, input().split())     # 주차 요금
times = [list(map(int, input().split())) for _ in range(3)]     # 각 차들이 들어오고 나간 시간
latest = 0     # 가장 늦게 떠난 차의 떠난 시간
for time in times:     # 이렇게 하지 말고 제한조건 확인 뒤 n = [0]*101 이렇게 작성해도 된다. (제한조건: 입력으로 주어지는 시간은 1과 100 사이) 
    if time[1] > latest:
        latest = time[1]

cars = [0] * latest     # 1시간 마다 차가 몇 대 있었는지를 기록 (각 시각이 아닌 1'시간'마다)

for time in times:
    arrive, leave = time[0], time[1]    
    for i in range(arrive, leave):     # 도착한 시각과 떠난 시각 사이의 차의 수를 1 증가시키기
        cars[i] += 1

answer = 0
for cnt in cars:
    if cnt == 1:
        answer += a
    elif cnt == 2:
        answer += 2 * b
    elif cnt == 3:
        answer += 3 * c

print(answer)    