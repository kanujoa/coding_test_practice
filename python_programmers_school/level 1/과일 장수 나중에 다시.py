def solution(k, m, score):
    cnt = [score.count(i) for i in range(1, k+1)]
    profit = 0
    a = len(cnt) - 1
    while True:
        if cnt[a] // m != 0:
            profit += cnt[a] * m * cnt[a] // m  
            cnt[a] -= m * cnt[a] // m
        elif cnt[a] // m == 0 and a == 0:
            break
        else:
            while cnt[a] // m == 0 or cnt[a] % m != 0:
                a -= 1
            profit += cnt[a] * m
            cnt[a] -= m - cnt[a+1]
    return profit

# print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))
print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))


# 시간 초과 코드
# def solution(k, m, score):
#     profit = 0
#     score.sort(reverse=True)
#     for _ in range(len(score) // m):
#         box = score[:m]
#         score = score[m:]
#         profit += box[-1] * m
#     return profit
