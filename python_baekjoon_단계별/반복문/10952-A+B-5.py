while True:
  a, b = map(int, input().split())
  if a == 0 and b == 0:     # a == b == 0으로도 작성 가능함.
    break
  print(a+b)
