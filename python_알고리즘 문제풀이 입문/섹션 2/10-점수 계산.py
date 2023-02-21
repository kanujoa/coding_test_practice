N = int(input())
confirm = list(map(int, input().split()))
score = [0] * N     # 각 문항의 점수를 나타낼 score 리스트 만들기 (길이는 문제의 개수인 N, 처음 값은 모두 0으로 초기화)

cur = confirm[0]     # 현재 값은 처음 채점 값인 confirm[0]으로 설정
if cur == 0:     # cur이 0이면 
  score[0] = 0     # 점수 처음 값은 0
else:     # cur이 1이면 
  score[0] = 1     # 점수 처음 값은 1

for i in range(1, N):     # 인덱스 i의 범위는 1부터 N-1까지 (0은 이미 앞에서 처리함)
  if confirm[i] == 1:     # 현재 채점 결과가 1일 때
    if confirm[i] == cur:     # 이전의 결과와 같으면 (앞이 1이면)
      score[i] = score[i-1] + 1     # 이전의 점수에 1을 더한 점수가 현재 인덱스의 점수
    else:     # 이전의 결과와 다르면 (앞이 0이면)
      score[i] = 1     # 점수는 1 (다시 1부터 시작)
    cur = 1     # 마지막에 cur을 1로 저장 (앞에서 미리 저장하면 confirm[i] == 1에서 의도치 않은 결과가 나온다.)
  else:     # 현재 채점 결과가 0일 때
    cur = 0     # 이전 결과와 상관없이(어차피 0이면 점수도 0이므로) 현재 값만 변화시켜줌

print(sum(score))