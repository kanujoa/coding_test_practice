n = int(input())
length = 2 * n - 1     # 별 찍기 최대 길이

for i in range(1, n+1):
    star = "*" * (i * 2 - 1)
    print(" " * ((length-len(star))//2) + star)
for i in range(1, n):
    star = "*" * (2 * (n-i) - 1)
    print(" " * ((length-len(star))//2) + star)
# 백준에서 오른쪽 공백을 만들면 출력 형식이 잘못되었다고 뜬다. 따라서 왼쪽만 공백을 만들어 주었다. (rjust 사용해도 됨.)

# 깔끔한 풀이
# a=int(input())
# for i in range(1,a+1):
#     print(' '*(a-i)+'*'*(2*i-1))     # a-i개의 공백을 출력하면 깔끔하다.
# for i in range(1,a):
#     print(' '*i+'*'*(2*a-2*i-1))     # i개의 공백을 출력하면 깔끔하다.