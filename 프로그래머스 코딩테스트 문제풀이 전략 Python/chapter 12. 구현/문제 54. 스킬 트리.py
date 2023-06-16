def solution(skill, skill_trees):
    answer = 0     # 정답 (가능한 스킬 트리 개수)
    for tree in skill_trees:
        i = 0     # skill에서 배울 스킬에 해당하는 인덱스 (몇 번째 순서인지 기록)
        for s in tree:
            if s in skill:     # skill에 있는 스킬이 나왔을 때
                if skill.index(s) == i:    # i와 skill에서의 s 위치(인덱스)가 같으면
                    i += 1     # 가능한 순서이므로 i 업데이트 
                else:     # 그렇지 않으면 불가능한 순서이므로
                    break     # 현재 스킬 트리 탐색 종료
        else:     # break 없이 빠져나오면 가능한 스킬 트리이므로
            answer += 1     # 정답 개수 1 추가
            
    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))