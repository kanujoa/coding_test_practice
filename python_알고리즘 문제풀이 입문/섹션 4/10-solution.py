# 현재 숫자보다 '큰' 숫자들이 '앞에 얼마나 존재해야 하느냐'가 중요하지 앞에서 이미 처리한 작은 숫자들이 현재 숫자의 뒤에 있는지 앞에 있는지는 상관이 없다!
# 입력된 자신보다 큰 숫자의 수는 리스트의 빈 공간(0)에 해당하고, 그 부분을 건너뛰어서 숫자를 배치해야 한다.
# 중간에 자신보다 작은 숫자 또한 건너뛴다. (이는 세는 것에 포함하지 않음.)

n = int(input())
a = list(map(int, input().split()))     # a : 역수열
seq = [0] * n     # seq 리스트는 길이가 n, 모든 요소가 0으로 초기화, 후에 채울 것임.
for i in range(n):     # i는 1부터 n-1까지 (인덱스)
    for j in range(n):     # j는 1부터 n-1까지 (인덱스)
        if a[i] == 0 and seq[j] == 0:     # 현재 숫자 앞의 수 중 더 큰 수의 개수가 0이고, s[j]가 빈 공간(0)일 때
            seq[j] = i + 1    # seq[j] 값을 현재 숫자인 i + 1의 값으로 변경
            break     # 반복문 빠져나가기
        elif seq[j] == 0:     # seq[j]가 빈 자리인 경우 (a[i]가 0이 아닐 때)
            a[i] -= 1     # a[i]에서 1을 뺀다.
for x in seq:
    print(x, end=" ")
            