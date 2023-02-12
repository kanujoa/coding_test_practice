n, m = map(int, input().split())     # n면체 m면체 입력받기
cnt = [0] * (n+m+3)     # cnt(count) 리스트 0으로 초기화, 길이는 n+m보다 큰 길이로 설정
max = -2147000000     # 가장 작은 값으로 max 초깃값 설정

for i in range(1, n+1):
  for j in range(1, m+1):
    cnt[i+j] += 1     # 나온 숫자의 합들은 cnt의 index에 해당하고, 그 부분의 count(cnt 리스트의 element)를 1씩 증가시킬 것임.

for i in range(n+m+1):     # index의 범위
  if cnt[i] > max:     # cnt[i]의 수가 max보다 크면
    max = cnt[i]     # max를 cnt[i]로 업뎃

for i in range(n+m+1):     
  if cnt[i] == max:     # cnt[i]가 이전에서의 가장 큰 count인 max와 같다면
    print(i, end=' ')     # 옆으로 해당하는 모든 수 출력