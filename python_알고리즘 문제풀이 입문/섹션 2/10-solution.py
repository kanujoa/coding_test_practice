n = int(input())     # 문제 수 입력받기
a = list(map(int, input().split()))     # 채점 결과 리스트

sum = 0     # 점수를 더한 결과
cnt = 0     # 가중치
for x in a:     # a 리스트의 요소 하나씩 x에 대입
  if x == 1:     # x가 1이면 
    cnt += 1     # cnt 1 증가
    sum += cnt     # sum에는 cnt값 더하기 (1이 연속으로 나왔을 경우를 처리 가능하다.)
  else:     # x가 0이면
    cnt = 0     # cnt를 0으로 하여 새로 출발하면 됨.

print(sum)
