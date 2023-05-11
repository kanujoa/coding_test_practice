def solution(answers):
    # 1. 학생들이 답을 찍는 규칙과 득점한 점수를 저장하는 배열, 그리고 가장 높은 득점을 한 학생들을 저장할 배열을 생성한다.
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    result = []

    # 2. 주어진 문제를 전부 채점한다.
    # 문제가 몇 문제가 나오든 학생들은 똑같은 규칙으로만 답을 제출할 것이므로 enumerate() 함수를 사용해 문제의 번호와
    # 정답을 한 번에 진행하면 된다.
    for idx, answer in enumerate(answers):
        if answer == student1[idx % len(student1)]:
            score[0] += 1
        if answer == student2[idx % len(student2)]:
            score[1] += 1
        if answer == student3[idx % len(student3)]:
            score[2] += 1

    # 3. 채점이 모두 끝났으면 가장 많은 점수를 득점한 학생을 뽑은 후 값을 반환한다.
    for idx, s in enumerate(score):     # score 배열에서도 enumerate를 사용해 직관적이고 편하게 코드를 작성한다.
        if s == max(score):
            result.append(idx + 1)
    return result