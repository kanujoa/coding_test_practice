N, K = map(int, input().split())     # 띄어쓰기로 input이 들어오면 map 함수를 이용해야 한다.

def result():
  divisor = [i for i in range(1, N+1) if N % i == 0]
  if len(divisor) < K :
    return -1
  else:
    return divisor[K-1]

print(result())