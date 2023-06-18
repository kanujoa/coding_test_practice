a, b, c = map(int, input().split())     # 각각 1대, 2대, 3대당 주차 요금
times = [list(map(int, input().split())) for _ in range(3)]     # 시간 입력받기(입력은 항상 3줄)

latest = 0     # 가장 마지막으로 트럭이 떠난 시간 구하기 (시간들 중 가장 큰 숫자)
for time in times:    
    for t in time:
        if t > latest:
            latest = t

trucks = [0] * latest     # 0부터 latest까지의 시간 간격을 나타내는 리스트, 각 요소는 각 시간 간격에 주차된 트럭의 수가 됨.
for time in times:
    arrive, leave = time[0], time[1]     # 도착한 시간, 떠난 시간
    for i in range(arrive, leave):     # arrive부터 leave 이전 숫자에 해당하는 인덱스 부분만
        trucks[i] += 1     # 주차된 트럭 수 1 증가

charge = 0     # 총 주차 요금 구하기
for truck in trucks:
    if truck == 1:     # 해당 시간 간격에 트럭이 1대 주차되어 있을 때
        charge += a
    elif truck == 2:     # 2대일 때
        charge += 2 * b
    elif truck == 3:     # 3대일 때 (시간이 0부터 시작하게 코드를 구성하였으므로 truck == 0인 경우도 있기 때문에 else라고 적으면 안되고 truck == 3으로 명시해야 한다.)
        charge += 3 * c

print(charge)