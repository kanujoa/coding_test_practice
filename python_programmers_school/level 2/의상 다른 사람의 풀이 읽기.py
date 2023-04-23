from itertools import combinations

def solution(clothes):
    answer = 0
    classify = {}
    for cloth, type in clothes:
        if type not in classify:
            classify[type] = [cloth]
        else:
            classify[type].append(cloth)
    for value in classify.values():
        if len(value) != 1:
            break
    else:
         return 2 ** len(classify.keys()) - 1   
    for i in range(1, len(classify)+1):
        tmp1 = 0
        combination = list(combinations(classify.keys(), i))
        for case in combination:
            tmp2 = 1
            for type in case:
                tmp2 *= len(classify[type])
            tmp1 += tmp2
        answer += tmp1
    return answer

# print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))


# 다른 사람의 풀이
def solution(clothes):
    clothes_type = {}

    for c, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2
        else:
            clothes_type[t] += 1

    cnt = 1
    for num in clothes_type.values():
        cnt *= num

    return cnt - 1