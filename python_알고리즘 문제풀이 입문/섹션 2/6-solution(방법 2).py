# 내가 푼 방법과 같은 방법 (함수 부분만 방법 1과 다르고 나머지는 다 같음.)
def digit_sum(x):
  sum = 0
  for i in str(x):
    sum += i
    return sum