N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

p1 = 0
p2 = 0
result = []
while p1 < N and p2 < M:     # N_list 또는 M_list의 요소들을 모두 result 리스트에 넣어지기 전까지 아래의 코드들이 실행됨.
  if N_list[p1] <= M_list[p2]:     # N_list에서의 p1 인덱스 요소가 M_list에서의 p2 인덱스 요소보다 작거나 같으면
    result.append(N_list[p1])     # result 리스트에 N_list의 p1 인덱스 요소를 추가
    p1 += 1      # 다음을 위해 p1도 1 증가
  else:     # M_list의 p2 인덱스 요소가 더 크면
    result.append(M_list[p2])     # result 리스트에 M_list의 p2 인덱스 요소를 추가
    p2 += 1     # 다음을 위해 p2도 1 증가
if p1 == N:     # p1이 N_list의 길이인 N과 같아지면 N_list의 요소들은 result에 모두 추가되었다는 의미이므로
  result += M_list[p2:]     # M_list의 나머지 모든 요소들을 result에 추가
else:     # p2가 M_list의 길이인 M과 같아지면 M_list의 요소들은 result에 모두 추가되었다는 의미이므로
  result += N_list[p1:]     # N_list의 나머지 모든 요소들을 result에 추가
for i in result:
  print(i, end=" ")