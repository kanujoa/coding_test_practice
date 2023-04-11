def check(student, answers):
    correct = 0
    for i in range(len(answers)):
        if answers[i] == student[i % len(student)]:
            correct += 1
    return correct

def solution(answers):
    res = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [check(one, answers), check(two, answers), check(three, answers)]
    maxx = max(score)
    for j in range(3):
        if score[j] == maxx:
            res.append(j+1)
    return res


# 위 코드 깔끔하게 작성하기
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result


# cycle 함수를 이용한 풀이
from itertools import cycle     # itertools에서 cycle 모듈을 불러온다.

def solution(answers):
    giveups = [      # 이렇게 패턴들을 하나의 리스트 안에 넣음으로써 공간복잡도까지 고려함.
        cycle([1,2,3,4,5]),
        cycle([2,1,2,3,2,4,2,5]),
        cycle([3,3,1,1,2,2,4,4,5,5]),
    ]
    scores = [0, 0, 0]
    for num in answers:
        for i in range(3):
            if next(giveups[i]) == num:
                scores[i] += 1
    highest = max(scores)

    return [i + 1 for i, v in enumerate(scores) if v == highest]