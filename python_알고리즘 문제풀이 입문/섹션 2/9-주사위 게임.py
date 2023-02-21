N = int(input())

reward = 0     # 상금이 가장 많은 사람 (for문이 끝날 때까지 업뎃 가능)
current = 0     # 현재 사람의 상금
for person in range(N):     # 사람 수의 범위
  dice = input().split()     # 숫자가 str type으로 변하여 리스트 안에 들어가게 된다. 케이스 하나 입력할 때마다 하나씩 출력되게 된다.
  for i in range(3):     # 3개의 주사위를 던지므로 한 사람 시행 당 결과 리스트 인덱스는 3개가 되어야 함.
    cur = dice[i]     # 현재 눈은 dice[i]
    if dice.count(cur) == 3:     # dice 리스트에서 현재 눈이 3개일 경우 (눈이 모두 같을 경우)
      current = 10000 + int(cur) * 1000     # 현재 상금
      break     # 바로 위 for문 빠져나가기 (다음 사람으로)
    elif dice.count(cur) == 2:     # dice 리스트에서 현재의 눈이 2개일 경우
      current = 1000 + int(cur) * 100     # 현재 상금
      break     # 바로 위 for문 빠져나가기
  else:     # dice 리스트에서 현재 눈이 1개여서 for문 break 없이 그대로 통과했을 경우
    num = int(dice[0])     # num의 초깃값이 dice[0]의 int형이라고 설정
    if int(dice[1]) > num:     # dice[1] int형이 위 dice[0]보다 크면 
      num = int(dice[1])     # num 업뎃
    if int(dice[2]) > num:     # dice[2] int형이 num보다 크면 (num은 상황에 따라 dice[0] 또는 dice[1]인 상태이다.)
      num = int(dice[2])     # 그걸로 num 업뎃
    current = num * 100     # 현재 상금 (세개의 눈 중 가장 큰 눈 * 100)
  if current > reward:     # 현재 상금이 지금까지의 가장 큰 상금보다 더 크다면 reward는 current 상금으로 업뎃
   reward = current

print(reward)     # 최종적인 reward 출력 (가장 큰 상금)