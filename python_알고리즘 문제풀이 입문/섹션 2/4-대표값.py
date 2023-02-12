N = int(input())
score = list(map(int, input().split()))
average = int(sum(score) / N + 0.5)     # round 사용하면 안됨!

gap = []     # 평균과의 차이를 담는 리스트

for i in range(0, len(score)):
  gap.append(score[i] - average)     

answer_gap = gap[0]     # 답이 될 점수에 해당하는 gap (옆에는 초깃값 설정한 것임)
index = 0     # 답이 될 index (옆에는 초깃값 설정한 것임)
for i in range(1, len(gap)):
  if abs(gap[i]) < abs(answer_gap):     # gap[i] 절댓값이 answer_gap 절댓값 보다 작으면 갭이 더 작아 평균에 더 가까운 것이므로
    answer_gap = gap[i]     # answer_gap 업데이트
    index = i     # index값도 업데이트
  elif abs(gap[i]) == abs(answer_gap):     # gap[i] 절댓값이 answer_gap 절댓값과 같은 경우
    if gap[i] > answer_gap:     # gap[i]가 answer_gap보다 크면(둘다 절댓값 X) gap[i]가 양수라는 것이므로 더 큰 점수임.
      answer_gap = gap[i]     # 더 큰 점수에 해당하는 gap이 answer_gap이 됨.
      index = i     # index 값도 업데이트
# gap[i]가 answer_gap과 부호까지 같은 수인 경우는 어차피 번호가 빠른 학생이 답이 되니 그냥 패스(안적어줘도 됨.)

print(average, index+1)     # 평균과 평균에 가장 가까운 학생의 번호 출력 (인덱스가 아닌 학생 번호 출력이므로 1을 더해줌.)