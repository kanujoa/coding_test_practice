T = int(input())     # 테스터 개수

for _ in range(T):
    H, W, N = map(int, input().split())     # 각각 호텔의 층수, 그 층의 방수, 몇 번째 손님인지를 나타냄
    for room in range(1, W + 1):
        for floor in range(1, H + 1):
            N -= 1
            if N == 0:
                if room < 10:
                    print(str(floor) + '0' + str(room))
                else:
                    print(str(floor) + str(room))
                break

# 더 간단한 풀이
T = int(input())     # 테스터 개수

for _ in range(T):
    cnt = 0
    H, W, N = map(int, input().split())     # 각각 호텔의 층수, 그 층의 방수, 몇 번째 손님인지를 나타냄
    while N > 0:
        N -= H     # 전체 층수를 한꺼번에 빼는 것을 반복
        cnt += 1     # 한 호실에 대한 전체 층수가 다 차면 방 번호가 1이 증가한다.
    N += H     # 0 이하의 값이 된 N에 전체 층수인 H를 더하면 어느 층수에 위치해야 하는지가 나옴.
    cnt = f'0{cnt}' if cnt < 10 else f'{cnt}'
    print(f'{N}{cnt}')

# 나머지와 몫으로도 해결하는 것이 가능!