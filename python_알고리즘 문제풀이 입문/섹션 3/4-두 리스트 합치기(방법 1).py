N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

result = N_list + M_list
for i in sorted(result):
  print(i, end=" ")

# 위처럼 sort 함수를 이용하여 호출하게 되면 nlog(n)만큼 돌게 된다.
# but 문제에서 이미 정렬이 되어 있고, 이것을 이용하면 n번만큼만 반복문이 돌면 된다.