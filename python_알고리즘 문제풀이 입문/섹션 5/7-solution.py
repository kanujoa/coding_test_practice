from collections import deque

need = input()     # 필수과목
n = int(input())     # 수업설계 과목 개수
for i in range(n):
    plan = input()     # 수업 설계
    dq = deque(need)     # 필수과목 string 하나하나로 큐 초기화함.
    for x in plan:     # x는 수업 설계 과목
        if x in dq:     # x가 dq(필수과목)의 요소와 일치하는 것이 있으면
            if x != dq.popleft():     # 그런데 x가 dq에서 pop하는 첫번째 요소와 다르면 순서가 다른 것이기 때문에
                print('#%d NO' %(i+1))     # 바로 NO 출력하고 끝
                break
    else:     # for문을 그냥 통과한 경우(순서 통과 경우)
        if len(dq) == 0:     # dq(필수과목)을 모두 pop시킨 경우
            print("#%d YES" %(i+1))     # 교육과정을 잘 맞게 짠 것이므로 YES 출력
        else:
            print('#%d NO' %(i+1))