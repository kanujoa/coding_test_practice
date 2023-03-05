a, b, c = map(int, input().split())

if a == b:
  if b == c:     # a == b == c
    print(10000 + b * 1000)
  else:     # a == b != c
    print(1000 + b * 100)
elif a == c:     # a == c != b (a == b == c인 경우는 앞에서 이미 걸러져서 a == c != b인 경우밖에 남지 않음.)
  print(1000 + a * 100)    
elif b == c:     # a != b == c (a == b == c 인 경우는 앞에서 이미 걸러지므로 옆 하나의 경우밖에 안됨.)
  print(1000 + b * 100)
else:     # a != b != c
  if a > b and a > c:     # a가 가장 큼
    print(a * 100)    
  elif b > a and b > c:     # b가 가장 큼
    print(b * 100)
  else:     # c가 가장 큼
      print(c * 100)