# 남학생(1): 스위치 번호가 자기가 받은 수의 배수이면 그 스위치의 상태를 바꾼다. (켜져 있으면 끄고, 꺼져 있으면 켠다.)
# 여학생(2): 받은 수와 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아 그 구간에 속한 스위치의 상태를 모두 바꿈.

switches = int(input())     # 스위치의 개수
states = list(map(int, input().split()))     # 스위치의 상태
students = int(input())     # 학생 수
numbers = [list(map(int, input().split())) for _ in range(students)]

for number in numbers:
    num = number[1]    
    if number[0] == 1:     # 남학생일 경우
        while num <= switches:     # num이 switchs의 범위를 초과하지 않을 때까지
            if states[num-1] == 1:     # 스위치가 켜져 있으면
                states[num-1] = 0     # 끄고
            else:     # 스위치가 꺼져 있으면
                states[num-1] = 1     # 켠다
            num += number[1]     # 다음 num은 number[1]의 배수 (num += num을 하면 1, 2, 4, 8 식으로 늘어나기 때문에 안된다!)
    else:     # 여학생일 경우
        if states[num-1] == 1:     # 해당 번호의 스위치가 켜져 있으면
            states[num-1] = 0     # 끄고
        else:     # 스위치가 꺼져 있으면
            states[num-1] = 1    # 켠다
        l = num - 2
        r = num
        while r <= switches - 1 and l >= 0:
            if states[l] == states[r]:
                if states[l] == 0 and states[r] == 0:
                    states[l] = 1
                    states[r] = 1
                else:
                    states[l] = 0
                    states[r] = 0
                l -= 1
                r += 1
            else:
                break

line = 0
if switches % 20 == 0:
    line = switches // 20
else:
    line = switches // 20 + 1
idx = 0
for _ in range(line):
    print(' '.join(map(str, states[idx: idx + 20])))
    idx += 20
            