n = int(input())
a = list(map(int, input().split()))

def digit_sum(x):     # a 리스트가 인수로 들어가게 된다.
  sum = 0     # 각 요소의 자릿수를 합친 값을 나타내기 위해 만든 변수 (초깃값 0)
  while x > 0:     # 각 자릿수의 합을 구하는 과정 (마지막에는 10보다 작은 수를 10으로 나눈 몫인 0에 다다르기 때문에 반복문 종료 가능) 
    sum += x % 10     # x를 10으로 나눈 나머지는 가장 오른쪽 자리 숫자가 됨.
    x = x // 10     # x를 10으로 나눈 몫은 구할 때마다 가장 오른쪽 자리 숫자를 없앰.
  # 즉, sum은 1의 자리 숫자, 10의 자리 숫자, 100의 자리 숫자..... 이 순서대로 누적되어 더한 결과가 됨.
  return sum

max = -2147000000     # 합이 가장 큰 element가 될 변수 max 정의 (초깃값은 가장 작은 값으로)
for x in a:     # a 리스트에 있는 요소들 하나씩 꺼내어 x에 대입
  total = digit_sum(x)     # 각 자릿수의 합은 digit_sum을 이용해 구하기 (즉, total == sum)
  if total > max:     # total이 이전 total 값인 max보다 더 클 때
    max = total     # max를 현재 total로 업뎃
    res = x     # 결과가 될 res도 현재 요소인 x로 업뎃

print(res)