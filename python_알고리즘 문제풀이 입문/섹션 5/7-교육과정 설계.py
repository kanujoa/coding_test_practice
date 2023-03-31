from collections import deque

essential = [e for e in input()]     # 필수과목 (순서 지켜야 함.)
n = int(input())     # 수업설계 과목 개수     
for i in range(1, n+1):
    design = deque(x for x in input())     # 수업 설계
    confirm = []
    while len(design) != 0:     # 수업 설계에 필수 과목이 빠져 있는 경우도 있을 수 있음을 고려!
        if design[0] in essential:
            confirm.append(design.popleft())
        else:
            design.popleft()
    if essential == confirm:
        print(f"#{i} YES")
    else:
        print(f"#{i} NO")