n, k = map(int, input().split())     # 띄어쓰기로 input이 들어오면 map 함수를 이용해야 한다.
cnt = 0

for i in range(1, n+1):
  if n % i == 0:
    cnt += 1
  if cnt == k:     # k번째로 작은 약수를 찾으면 i를 출력하고 break한다. (위 if문이 fasle면 실행되는 것이 아니라 for문 실행 시 항상 실행되어야 하기 때문에 elif가 아닌 if로 적어줌.)
    print(i)
    break     # but 약수의 개수가 k보다 작은 경우 break가 되지 않고 for문이 끝나게 된다.
else:     # for else 문을 이용하여 해결 --> for문이 break가 걸리지 않고 정상적으로 끝나면 이 else문이 실행되게 된다.
  print(-1)
