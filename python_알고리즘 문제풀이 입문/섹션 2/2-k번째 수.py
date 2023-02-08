T = int(input())

for i in range(1, T+1):
  N, s, e, k = map(int, input().split())
  numbers = map(int, input().split())
  numbers = sorted(list(numbers)[s-1:e])     # 컴퓨터는 0부터 세므로 항상 -1씩 해주어야 함. (ex) 2번째를 원하면 -1해서 index 1을 입력해 주어야 함.)
  print(f"#{i} {numbers[k-1]}")     # 출력 형식이 있으면 출력 형식까지 갖추어야 함.
  