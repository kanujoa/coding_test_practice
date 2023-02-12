n = int(input())     # 학생 수 n 입력받기
a = list(map(int, input().split()))     # 학생들의 점수를 입력받아 a 리스트로 만들기
ave = int(sum(a) / n + 0.5)     # 평균 구하기
min = 2147000000     # 4byte에서 가장 큰 정수값

for idx, x in enumerate(a):     # enumerate : index 값(idx)과 그 index에 해당하는 a 리스트에서의 값(x)이 쌍으로 나오게 함.
  tmp = abs(x - ave)     # 학생 점수와 평균과의 갭의 절댓값을 tmp라는 임시 변수에 저장함.
  if tmp < min:     # 갭이 min보다 작으면 그것이 min에서의 점수보다 평균에 가까운 것이 되므로
    min = tmp     # min을 tmp로 업뎃
    score = x     # score 변수 생성, 값은 현재 점수인 x가 됨.
    res = idx + 1      # 결과에 해당하는 학생 번호는 현재 index인 idx에 1을 더한 값
  elif tmp == min:     # 갭이 같은 경우
    if x > score:     # 현재 점수 x가 전에 저장된 점수인 score보다 크다면 
      score = x     # 더 큰 수인 현재 점수 x가 score로 업뎃
      res = idx + 1     # 학생 번호도 업뎃

print(ave, res)

# round는 round_half_even 방식! 정확하게 .5일 경우 정수 부분이 짝수이면 소수점 아래는 버리고 정수 그대로, 홀수이면 소수점 아래 버리고 정수 부분에 1을 더해줌.
# ex 1) round(4.5) --> 4
# ex 2) round(5.5) --> 6
# ex 3) round(4.511)  --> 5
# 우리는 .5이면 무조건 반올림되는 것을 원하므로 round를 사용하면 안되고 위 코드처럼 작성해야 한다.