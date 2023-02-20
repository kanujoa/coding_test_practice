N = int(input())
numbers = list(map(int, input().split()))

def reverse(x):
  reverse = []
  for num in x:
    element = str(num)[::-1]
    for j in element:
      if j == "0":
        element.replace(j, "")
      else: 
        break
    reverse.append(int("".join(element)))
  return reverse


def isPrime(x):
  for rvs_num in reverse(numbers):
    prime_num = []
    if rvs_num == 2 | rvs_num == 3:
      prime_num.append(rvs_num)
    elif rvs_num == 1:
      pass
    else:
      for i in range(2, rvs_num):
        if rvs_num % i == 0:
          break
      else:
        prime_num.append(rvs_num)
    for result in prime_num:
      print(result, end = " ")
      
isPrime(numbers)