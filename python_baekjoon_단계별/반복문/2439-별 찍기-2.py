# import sys
# input = sys.stdin.readline     --> 입력 범위가 작으면 굳이 사용하지 않아도 됨.
n = int(input())
for i in range(1, n+1):
    print(" " * (n-i) + "*" * i)

# rjust 메서드를 활용해 본 풀이 (문자열의 오른쪽을 공백으로 채워서 길이가 n인 문자열을 만듦, 이게 좀 더 빠름)
n = int(input())
for i in range(1, n+1):
    star = i * "*"
    print(star.rjust(n, " "))

# 다른 풀이
# n=int(input())
# [print(' '*(n-i)+'*'*i)for i in range(1,n+1)]