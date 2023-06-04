# 1부터 10000까지 모든 숫자를 탐색하여 각각을 생성자로 가지는 수를 리스트에 체크한다.

ch = [0] * 10000

for num in range(1, 10001):
    idx = num + sum(list(int(n) for n in str(num))) - 1
    if idx < 10000:
        ch[idx] = 1

for idx in range(10000):     
    if ch[idx] == 0:
        print(idx + 1)