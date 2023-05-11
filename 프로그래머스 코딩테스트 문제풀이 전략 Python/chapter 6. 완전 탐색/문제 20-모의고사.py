def check(student, answers):
    correct = 0
    length = len(student)
    for i in range(len(answers)):
        if student[i % length] == answers[i]:
            correct += 1
    return correct

def solution(answers):
    result = []
    s_1 = [1, 2, 3, 4, 5]
    s_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    correct_cnt = [check(s_1, answers), check(s_2, answers), check(s_3, answers)]
    _max = max(correct_cnt)
    for i in range(3):
        if correct_cnt[i] == _max:
            result.append(i + 1)
    return result

print(solution([1,2,3,4,5]))