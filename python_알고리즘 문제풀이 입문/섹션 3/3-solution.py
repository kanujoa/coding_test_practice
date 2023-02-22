a = list(range(21))     # range(21)을 사용하면 0부터 20까지의 요소가 있는 리스트 생성

for _ in range(10):     # _를 해주게 되면 변수가 없는 것이 됨. i같은 변수를 쓰면 그 변수에 대입하면서 도는 것도 시간이 걸리기 때문에 활용하지 않을 때는 _를 작성함.
  s, e = map(int, input().split())     # 구조분해할당
  for i in range((e-s+1)//2):
    a[s+i], a[e-i] = a[e-i], a[s+i]     # 스와프
a.pop(0)     # 0번 인덱스에 있는 것을 pop함. (0을 제거함.)
for x in a:
  print(x, end=" ")