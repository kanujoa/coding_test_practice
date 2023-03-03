from sys import stdin
N, M = map(int, stdin.readline())
num = list(map(int, stdin.readline()))

# 정렬하기
play  = True
a = 0     # 비교 기준이 되는 인덱스
b = 1     # a와 크기를 비교할 숫자의 인덱스
while play:
  if a < N:     # a가 리스트의 길이인 N보다 작으면
    if b < N:     # b도 N보다 작으면
      if num[a] > num[b]:     # a번째 숫자가 b번째 숫자보다 크면
        num.insert(a, num.pop(b))     # b번째 숫자를 뽑아내어 a번째 숫자 바로 앞에 삽입 (b번째 숫자는 pop으로 제거됨.)
        b += 1     # 다음 숫자 비교를 위해 b 증가
      else:     # 두 숫자가 같거나 a번째 숫자가 b번째 숫자보다 작으면 움직일 필요가 없으므로
        b += 1     # 다음 숫자 비교를 위해 b 증가
    else:     # b가 최대 범위를 벗어나면
      a += 1     # 기준 숫자를 바꾸기 위해 a에 1 추가 (인덱스 한칸 이동)
      b = a + 1     # b도 a 한칸 옆으로 이동
  elif a >= N:     # a가 범위에서 벗어나는 순간이 오면
    play = False     # play가 False로 변하면서 반복문 종료
  
# 정렬 후 M의 위치 번호를 출력하기
print(num.index(M) + 1)     # 정렬된 num 리스트에서 M의 인덱스 번호를 찾고 그것에 1을 더한 값이 답임.