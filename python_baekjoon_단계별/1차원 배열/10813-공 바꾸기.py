import sys
input = sys.stdin.readline
n, m = map(int, input().split())
basket = [i for i in range(n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    basket[i], basket[j] = basket[j], basket[i]
basket.pop(0)
for x in basket:
    print(x, end=" ")

# 아래 값 출력 부분을 다음과 같이 join(공백으로 문자 사이를 띄어줌)과 map 메서드(buckets의 요소들을 str type으로 바꿔줌)를 이용해 작성할 수도 있다.
# print(' '.join(map(str, buckets)))