# 중간에 디버깅용으로 불필요한 코드를 작성하지는 않았는지 꼭 확인하기!!

from collections import deque

def check_cloud_exsist(weather):
    for r in range(h):
        for c in range(w):
            if weather[r][c] == 'c':
                return True
    return False

def move_clouds(weather):
    for r in range(h):
        weather[r].appendleft('.')
        weather[r].pop()
    return weather

h, w = map(int, input().split())     # h는 높이(행의 수), w는 너비(열의 수)
weather = [deque(item for item in input()) for _ in range(h)]
answer = [[-1] * w for _ in range(h)]
cnt = 1
while True:
    for r in range(h):
        for c in range(w):
            if weather[r][c] == 'c' and answer[r][c] == -1:
                answer[r][c] += cnt
    weather = move_clouds(weather)          
    if check_cloud_exsist(weather) == False:
        for i in range(h):
            print(' '.join(map(str, answer[i])))
        break
    cnt += 1