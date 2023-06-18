t = int(input())     # 테스트 케이스의 개수

for _ in range(t):
    n = int(input())     # 참가 선수의 수
    order = list(map(int, input().split()))     # 결승선을 통과한 선수들의 순서 (팀명으로 기록)
    teams = set(order)     # 팀명만 추출
    
    include = {}     # 점수 계산에 포함시키는 팀들
    for team in teams:
        if order.count(team) == 6:     # 해당 팀의 참가 선수가 6명이면
            include[team] = []     # 점수 계산에 포함시키기
    grade = 1     # 현재 등수
    for team in order:     # order 리스트에서의 팀을 순서대로 탐색
        if team in include:     # 해당 팀이 점수 계산에 포함되는 팀이라면
            include[team].append(grade)     # 해당 팀을 key로 하는 value 리스트에 현재 등수 추가
            grade += 1     # 다음을 위해 등수 하나 내리기
    
    top_four = {}     # 상위 4명 선수의 등수 합을 저장하는 딕셔너리 (key: 팀명, value: 등수 합)
    for team in include:
        top_four[team] = sum(include[team][:4])
    grade_sum = list(top_four.values())     # 4명의 점수 합만을 뽑아낸 리스트
    if grade_sum.count(min(grade_sum)) == 1:     # 등수 합이 가장 작은 팀이 한 팀이라면 (동점이 없다면)
        for team in include:
            if top_four[team] == min(grade_sum):
                print(team)     # 그 팀명을 출력
    else:     # 등수 합이 가장 작은 팀이 여러 팀이라면 그 팀중 5번째 주자가 가장 빨리 들어온 팀이 우승이다. (5번째 주자의 등수만 살피기)
        same = []
        for team in include:
            if top_four[team] == min(grade_sum):      # 등수가 가장 작은 팀들일 경우
                same.append(team)     # same 리스트에 추가
        fifth = {}     # 5번째로 들어온 주자의 등수를 기록하는 딕셔너리 (key: 등수, value: 팀명)
        for team in same:
            fifth[include[team][4]] = team
        print(fifth[min(fifth.keys())])     # 5번째 주자가 가장 작은 등수를 가지는 팀을 출력        
        print(same)
        print(fifth)