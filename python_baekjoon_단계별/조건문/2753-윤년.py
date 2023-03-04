y = int(input())

if y % 4 == 0:
  if y % 400 == 0:
    print(1)
  elif y % 100 != 0:
    print(1)
  else:
    print(0)
else:
  print(0)

# 다른 풀이
# n = int(input())     
# print(int(n%400==0 or (n%4==0 and n%100!=0)))     --> True와 False를 int형으로 변환하여 값을 출력하는 코드이다. 0 또는 1로 출력된다.
# int 함수 안에는 문제에서 나온 윤년이 될 수 있는지를 확인하는 조건이 그대로 있다.