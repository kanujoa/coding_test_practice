# 이미 다 줄이 세워져 있는 상태에서 자리를 변경하고 마련하는 것이 아니라 한명씩 뒤로 줄을 세워야 함!

p = int(input())     # 테스트 케이스의 개수

for _ in range(p):
    cnt = 0     # 뒤로 물러난 횟수 (cnt는 테스트 케이스가 새로 주어질 때마다 초기화해야 하는 것 잊지 않기!)
    info = list(map(int, input().split()))
    case_num = info[0]
    height = []
    for i in range(1, len(info)):
        cur_h = info[i]     # 현재 학생의 키
        if len(height) == 0 or max(height) < cur_h:     # 줄이 비어 있거나 앞의 학생들이 모두 현재 학생보다 키가 작을 경우
            height.append(cur_h)     # 그냥 뒤에 세우기
        else:     # 앞에 현재 학생보다 키가 큰 학생이 있는 경우
            for h in height:
                if h > cur_h:     
                    height.insert(height.index(h), cur_h)     # 가장 앞에 있는 현재 학생보다 키가 큰 학생의 순서에 현재 학생이 들어간다.
                    cnt += (len(height) - height.index(cur_h) - 1)     # 한걸음 물러나는 학생의 수는 현재 학생의 자리에서부터 맨 뒷자리에 있는 학생까지
                    break
    print(case_num, cnt)