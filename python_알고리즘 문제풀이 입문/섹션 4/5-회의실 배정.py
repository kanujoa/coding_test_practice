# 실패... (정렬 시 시작 시간을 기준으로 정렬한 것이 문제! 회의 시간이 더 긴 선택을 하면 안되기 때문에 끝나는 시간을 기준으로 정렬해야 함.)

import sys
input = sys.stdin.readline
n = int(input())     # n = 회의의 수
time = []     # time 리스트: 회의 시작시간과 끝나는 시간을 묶은 것을 원소로 하는 리스트 (time[i][0] = 시작 시간, time[i][1] = 끝나는 시간)
for _ in range(n):
  time.append(list(map(int, input().split())))     # 시작시간, 끝나는 시간 순으로 입력
time.sort()     # 회의 시간이 오름차순으로 정렬되도록 sort 해줌

def Count(time):
  for c in range(n):     # c = time 리스트에서 첫 번째로 고른 회의시간
    cur = time[c]     # cur = 현재 고른 회의 시간(list)
    x = c + 1      # x = 다음으로 고를 회의 시간(int(index))
    cnt = 1     # 사용할 수 있는 회의 수(하나는 꼭 고르므로 1부터 시작)
    while x < n:     # x가 n 보다 작을 때까지 반복 (x의 index가 n의 길이보다 작아 범위를 초과하지 않을 때까지)
      if time[x][0] >= cur[1]:     # 다음으로 고를 회의의 시작 시간이 현재 고른 회의의 끝나는 시간보다 크거나 같으면
        cnt += 1     # 회의 수 1 증가
        cur = time[x]     # 현재 고른 회의 변경
        x += 1     # 다음 회의를 고르기 위해 x도 1 증가
      else:     # 조건에 만족하지 않는 경우
        x += 1     # x만 1 증가
  return cnt

res = 0
if Count(time) > res:     # 가능한 회의 수가 res에 저장된 수보다 크면
  res = Count(time)     # res를 cnt의 수로 바꾸기

print(res)