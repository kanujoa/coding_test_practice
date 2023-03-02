n, m = map(int, input().split())
a = list(map(int, input().split()))
lt = 0     # (포인터 2개 설정) 왼쪽에 위치하는 포인터 lt
rt = 1     # 오른쪽에 위치하는 포인터 rt
tot = a[0]     # 합을 나타내는 변수 tot(초깃값은 a 리스트의 첫번째 원소로 설정)
cnt = 0     # 조건에 맞는 수를 세기 위한 변수 cnt
while True:     # Ture일 때까지 반복 (후에 False로 바뀌는 때나 break가 오면 반복문 종료)
  if tot < m:     # tot가 문제에서 요구되는 합인 m보다 작을 때
    if rt < n:     # rt가 리스트의 길이를 나타내는 n보다 작다면
      tot += a[rt]     # tot에 a[rt]의 값을 더한다.
      rt += 1     # rt는 오른쪽으로 한 칸 이동했으므로 rt에 1을 더해준다.
    else:     # rt가 n과 같거나 커질 때는 이미 모든 원소를 다 돌아 본 것이기 때문에
      break     # break로 while문을 벗어난다.
  elif tot == m:     # tot가 m값과 같아지면 
    cnt += 1     # cnt 1 증가
    tot -= a[lt]     # tot에 a[lt] 빼기
    lt += 1     # lt 오른쪽으로 한 칸 이동해야 하므로 lt에 1을 더해줌. (현재 lt 상태에서 더 더해봤자 더 큰값이 나오므로 필요 X, 따라서 다음 lt로 넘어감.)
  else:     # tot가 m보다 커지면
    tot -= a[lt]     # tot에서 a[lt] 만큼을 빼준다. 
    lt += 1     # lt가 1 증가

print(cnt)
