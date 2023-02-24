# 첫번째 리스트와 두번째 리스트에서 각각의 인덱스를 가리키는 포인터 2개가 필요하다. (p1, p2)
# ex) a[p1] <= b[p2] 이면 a[p1]을 결과 리스트인 c의 요소로 추가시킨다. 그리고 p1+1이 된다. (p2는 그대로, 수가 같을 경우에는 아무 숫자나 들어가도 된다.)
# 반대의 경우 반대 리스트의 숫자가 들어감.
# ex) p1이 끝났을 경우 b 리스트의 남은 숫자들을 모두 붙여버리면 됨.

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
p1 = p2 = 0     # 이렇게 한줄로 적어줄 수도 있다.
c = []
while p1 < n and p2 < m:
  if a[p1] <= b[p2]:
    c.append(a[p1])
    p1 += 1
  else:
    c.append(b[p2])
    p2 += 1
if p1 < n:
  c = c + a[p1:]
if p2 < m:
  c = c + b[p2:]
for x in c:
  print(x, end=" ")