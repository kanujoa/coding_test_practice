# 기본은 재귀함수를 이용하여 순열과 조합을 만들어내는 방법을 알고 있어야 한다.
# 실제 코딩 테스트에서 라이브러리를 사용하지 못하게 막아놓았을 수도 있기 때문이다.

import itertools as it

n, f=map(int, input().split())
b=[1]*n
for i in range(1, n):
    b[i]=b[i-1]*(n-i)/i
a=list(range(1, n+1))
for tmp in it.permutations(a):
    sum=0
    for L, x in enumerate(tmp):
        sum+=(x*b[L])
    if sum==f:
        for x in tmp:
            print(x, end=' ')
        break