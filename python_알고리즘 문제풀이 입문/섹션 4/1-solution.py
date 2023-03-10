# 이분 탐색 : 리스트의 맨 왼쪽 인덱스를 나타내는 lt, 맨 오른쪽 인덱스를 나타내는 rt, 중간 인덱스를 나타내는 mid 필요!
# mid = (lt + rt) // 2     --> 문제에서 lt = 0, rt = 7이므로 mid는 3이 됨.
# 정렬된 리스트라고 할 때 그 리스트의 mid값이 M이라면 mid+1의 값을 출력하도록 하면 된다.
# but 값이 M보다 클 경우, rt를 mid 바로 이전 인덱스값으로 옮긴다. 그리고 그 범위에서 mid를 다시 설정
# 만약 값이 M보다 작을 경우, lt를 현재 mid 바로 다음의 인덱스값으로 이동시킨다. 그리고 그 범위에서 mid를 다시 설정
# 이렇게 계속 절반 범위씩을 버려간다.

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()     # 정렬은 그냥 sort 이용
lt = 0     # 맨 왼쪽 인덱스
rt = n-1     # 맨 오른쪽 인덱스 (리스트의 길이는 a)

while lt <= rt:     # lt가 rt보다 커지면 이분 탐색이 불가하므로 이분 탐색이 종료된 것과 마찬가지!
  mid = (lt + rt) // 2     # 중간 지점 인덱스
  if a[mid] == m:     # (정렬된 리스트)a 리스트에서 mid값이 m이면 답을 찾은 것
    print(mid+1)     # 번째수를 찾아야 하므로 +1 하여 출력
    break
  elif a[mid] > m:     # mid 부분의 값이 m보다 크면 mid보다 앞 인덱스에서 값을 찾아야 함. --> rt를 조정해야 함.
    rt = mid - 1
  else:     # mid 부분의 값이 m보다 작으면 mid보다 뒤 인덱스에서 값을 찾아야 함. --> lt를 조정해야 함.
    lt = mid + 1