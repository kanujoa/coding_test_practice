def solution(lottos, win_nums):
    rank  = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    cnt = 0
    for n in lottos:
        if n in win_nums:
            cnt += 1
            win_nums.remove(n)
    return [rank[cnt+lottos.count(0)], rank[cnt]]


# 다른 풀이
# def solution(lottos, win_nums):
#     rank = {
#         0: 6,
#         1: 6,
#         2: 5,
#         3: 4,
#         4: 3,
#         5: 2,
#         6: 1
#     }
#     return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]
# set을 이용해 중복을 제거한 lottos와 중복을 제거한 win_nums의 교집합 원소의 개수에 lottos에 들어있는 0의 개수를 합한 값을 
# rank의 key로 하면 최대 등수가 나오고, 그냥 교집합 원소의 개수를 key로 하면 최소 등수가 나온다.
# 문제에서 0을 제외한 다른 숫자들은 2개 이상 존재하지 않는다고 하였다. 따라서 set 쓰는 것이 가능! 