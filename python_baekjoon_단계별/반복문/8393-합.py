n = int(input())
s = 0
for i in range(1, n+1):
    s += i
print(s)

# 짧은 풀이
# print(sum([i for i in range(1, int(input())+1)]))

# 반복문을 사용하지 않는 풀이 (수학 공식 이용하기)
# n = int(input())
# print(n * (n+1) // 2)