N, M = map(int, input().split())

sum = []
for a in range(1, N+1):
  for b in range(1, M+1):
    sum.append(a+b)     # N면체와 M면체에서의 가능한 모든 숫자의 합을 sum 리스트에 추가함.

count = 0     # count 초깃값
result = []     # result 초깃값 (빈 리스트)
for item in set(sum):     # sum 리스트에 set을 사용해 요소 중복 제거하여 거기에서의 요소들 하나하나가 item 변수에 들어감.
  tmp = sum.count(item)
  if tmp > count:     # 서로 다른 요소들이 sum 리스트에서 몇개가 있는지를 count함. 그리고 그것이 count보다 크면
    count = tmp     # count값을 현재 sum.count로 업뎃
    result.clear()     # 리스트의 이전 원소들 모두 삭제
    result.append(item)     # 결과값은 item이 됨.
  elif tmp == count:     # 요소의 개수가 전이랑 같을 경우
    result.append(item)     # 전이랑 이어서 sum 값(item) 추가

for res in result:
  print(res, end=" ")      # 한 줄의 result 안의 요소들을 모두 출력 