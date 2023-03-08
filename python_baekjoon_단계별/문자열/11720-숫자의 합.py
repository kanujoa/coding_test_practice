n = int(input())
number = str(int(input()))
res = 0
for i in number:
    res += int(i)
print(res)

# 더 짧고 빠른 풀이
# n = int(input())
# print(sum([int(f) for f in input()]))     --> 리스트 이용한다.

