n = int(input())     # 사람 수 입력받기

res = 0     # 큰 상금 결과 저장
for i in range(n):
  tmp = input().split()
  tmp.sort()     # 주사위 수가 담긴 리스트가 오름차순 정렬 --> 다 다른 눈이 나왔을 때 가장 큰 수를 고르기 쉽게 (여기서는 str type이다.)
  a, b, c = map(int, tmp)      # 오름차순 정렬된 tmp 리스트의 요소들을 int로 형변환하여 a, b, c 변수에 차례로 할당
  if a == b and b == c:     # 눈이 모두 같은 경우
    money = 10000 + a * 1000
  elif a == b or a == c:     # a와 같은 눈이 하나 있을 경우 (두 개의 눈이 같을 경우 1)
    money = 1000 + a * 100
  elif b == c:     # b와 c의 눈이 같을 경우 (두 개의 눈이 같을 경우 2)
    money = 1000 + b * 100     
  else:     # 세 개의 눈이 모두 다를 경우
    money = c * 100
  if money > res:     # 현재 상금이 res보다 크면
    res = money     # res = money이다.

print(res)

