def hanoi(n, start, to, mid, process):
    global cnt
    if n == 1:
        cnt += 1
        return process.append([start, to])
    hanoi(n - 1, start, mid, to, process)
    cnt += 1
    process.append([start, to])
    hanoi(n - 1, mid, to, start, process)

n = int(input())
cnt = 0
process = []
hanoi(n, 1, 3, 2, process)
print(cnt)
for item in process:
    print(' '.join(map(str, item)))