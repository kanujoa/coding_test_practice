A = int(input())

if A >= 90:
  print("A")
elif A >= 80:
  print("B")
elif A >= 70:
  print("C")
elif A >= 60:
  print("D")
else:
  print("F")

# 다른 풀이
# print('FFFFFFDCBAA'[int(input())//10])     
# 0, 10, 20 ~ 100 점대까지 구간을 나누어 점수를 문자열로 나타낸 후 인덱싱을 이용하여 값 출력
# 문자열의 길이는 10이다. 인덱싱은 점수를 입력받아 10으로 나누어 나온 몫을 이용해 하면 됨.  