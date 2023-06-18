n, new_score, p = map(int, input().split())     # 리스트에 있는 점수의 개수, 새로운 점수, 리스트에 올라갈 수 있는 점수의 개수

if n == 0:     # 리스트에 있는 점수의 개수가 없다면
    print(1)     # 새로운 점수는 무조건 1등이 되므로
    exit()     # 프로그램 종료

scores = list(map(int, input().split()))     # 이미 존재하는 점수 리스트
scores.sort(reverse=True)     # 점수 오름차순 정렬

def get_grade(scores, new_score):     # 등수를 구하는 함수
    scores.append(new_score)     # 새로운 점수는 무조건 리스트에 올라갈 수 있다.
    scores.sort(reverse=True)     # 점수 리스트 다시 내림차순 정렬 
    cnt = 1     # 동일한 점수가 나오는 횟수 (본인 포함)
    grade = 0     # 등수
    for i in range(len(scores)):
        if i == 0:     # 첫번째 점수는 무조건 1등
            grade += cnt
        else:     # 첫번째 점수가 아닐 경우 이전 점수를 살펴보아야 함.
            if scores[i] == scores[i-1]:     # 이전 점수와 동일할 경우 
                cnt += 1     # 등수는 그대로, cnt만 증가
            else:
                grade += cnt     # 지금까지 누적된 동일한 점수가 나오는 횟수만큼 등수가 내려감.
                cnt = 1     # cnt는 다시 1로 초기화
        if scores[i] == new_score:     # 현재 점수가 새로운 점수와 같다면 
            print(grade)     # 새로운 점수의 등수를 출력하고
            return      # 함수 종료

if len(scores) < p:     # 이미 존재하는 점수의 수가 리스트에 올라갈 수 있는 점수의 개수보다 작으면
    get_grade(scores, new_score)     # 등수 구하는 함수 실행
else:     # 점수 리스트가 꽉 차있다면
    if scores[-1] >= new_score:     # 점수 리스트에서 가장 작은 점수보다 현재 점수가 더 작거나 같다면 
        print(-1)     # 새로운 점수가 리스트에 올라가는 것이 불가능하므로 -1 출력 후 끝
    else:     # 그렇지 않을 경우
        scores.pop()     # 가장 작은 점수 제거
        get_grade(scores, new_score)     # 등수 구하는 함수 실행
