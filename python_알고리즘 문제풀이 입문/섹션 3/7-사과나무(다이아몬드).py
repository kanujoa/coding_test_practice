N = int(input())
num = [list(map(int, input().split())) for _ in range(N)]    # 2차원 리스트로 격자판의 수들 담기

half = len(num) // 2     # 가운데 인덱스가 될 숫자
result = 0     # 총합의 결과가 담길 변수
for i in range(half+1):     # 인덱스의 범위 (5줄일 경우 0, 1, 2까지 돌아야 함. 위아래 한꺼번에 갈 것이므로)
  if i == half:     # 인덱스가 half와 같아질 경우 가운데 한 줄에 해당하기 때문에
    result += sum(num[i])     # 그 줄의 숫자를 다 더해서 result에 더해줌.
  else:     # 보통의 경우 (가운데 줄이 아니어서 위아래 동시에 계산 가능할 경우)
    result += (sum(num[i][half-i : half+i+1]) + sum(num[-i-1][half-i : half+i+1]))     # 위쪽 끝, 아래쪽 끝부터 동시에 돌고, 가운데로 갈수록 더해야 할 요소들이 2개씩 늘어나야 한다.
print(result)