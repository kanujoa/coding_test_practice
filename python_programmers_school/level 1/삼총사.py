def solution(number):
    angels = 0     # 가능한 삼총사의 수
    for i in range(len(number)-2):
        for j in range(i+1, len(number)-1):
            for z in range(j+1, len(number)):
                if number[i] + number[j] + number[z] == 0:
                    angels += 1
    return angels


# 모듈을 이용한 풀이
# def solution (number) :
#     from itertools import combinations     # --> itertools 모듈에 있는 combinations를 불러온다. (조합을 구하기 위해)
#     cnt = 0
#     for i in combinations(number,3) :     # --> number 리스트에서 3개의 수를 조합하라는 의미 (i에는 3개의 수가 튜플 형태로 들어감.)
#         if sum(i) == 0 :
#             print(i)
#             cnt += 1
#     return cnt
# print(solution([-2, 3, 0, 2, -5]))
# permutations를 import 하면 순열을 구할 수 있다.