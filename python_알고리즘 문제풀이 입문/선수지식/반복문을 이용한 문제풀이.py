'''
반복문을 이용한 문제풀이
1) 1부터 N까지 홀수출력하기
2) 1부터 N까지의 합 구하기
3) N의 약수출력하기
'''
'''
n = int(input())     # 그냥 input만 적으면 string 형태로 나간다.
for i in range(1, n+1):      # 1부터 N까지
    print(i)
'''
'''
1)
n = int(input())
for i in range(1, n+1):
    if i % 2 == 1:
        print(i)
'''
'''
2)
n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)
'''
'''
3)
n = int(input())
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=" ")
'''
