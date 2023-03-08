# 실패 ...

import sys
input = sys.stdin.readline

n, m = map(int, input().split())     # n: 곡의 수, m: 노래를 넣을 DVD 개수
songs = list(map(int, input().split()))     # n개의 곡의 각각의 길이

s = 0     # s는 songs 리스트의 노래 시간을 더한 것을 저장할 변수
dvd = 0     # 아래의 time과 일치하여 하나의 DVD가 완성된 횟수
lt = 0     # lt는 time의 최솟값
rt = sum(songs)     # rt는 songs 리스트에 있는 노래 시간을 모두 더한 값 (time의 최댓값)
tmp = 0     # 더 적은 수의 dvd를 구하기 위한 임시 변수
res = 0     # tmp 개수의 dvd에 해당하는 시간을 저장하기 위한 변수

while lt <= rt:
    time = (lt + rt) // 2     # 각 DVD에 들어갈 노래의 시간을 time으로 설정 (앞에서의 mid와 같은 의미, 여기서는 평균 시간으로 설정)
    for song in songs:
        s += song
        if s == time:     # 리스트에 있는 노래의 시간들을 합친 것이 time과 같으면
            dvd += 1     # dvd 1개 완성이므로 dvd 1증가
            s = 0     # s 다시 0으로 초기화
        elif s > time:     # s가 time과 같아지지 않고 시간을 넘어버린다면 time이 애초에 답이 아니다.
            break     # 반복문 즉시 빠져나옴
    if dvd == m:
        if dvd < tmp:     # tmp 값보다 dvd 개수가 더 작다면
          tmp = dvd     # tmp 값 업데이트
          res = time     # res에 tmp와 대응하는 time값 저장
          s = 0
        break
    elif dvd > m:     # dvd의 개수가 원하는 개수 m보다 많이 만들어지면 time을 더 늘려야 한다.
        lt = time
        dvd = 0
        s = 0
    elif dvd < m:     # dvd의 개수가 원하는 개수 m보다 적게 만들어지면 time을 더 줄여야 한다.
        rt = time
        dvd = 0  
        s = 0     

print(res)         