n = int(input())     # 시그널의 길이
_input = input()     # 시그널 입력받기
signal = ''      # 시그널의 세로 줄을 왼쪽에서부터 순서대로 읽어가며 변형하기
for i in range(n // 5):
    for j in range(i, n, n // 5):
        signal += _input[j]

num = {     # 각 숫자의 시그널을 딕셔너리로 만들기 (세로 줄을 왼쪽에서부터 순서대로 읽어가며)
    '######...######' : '0',
    '#####' : '1',
    '#.####.#.####.#' : '2',
    '#.#.##.#.######' : '3',
    '###....#..#####' : '4',
    '###.##.#.##.###' : '5',
    '######.#.##.###' : '6',
    '#....#....#####' : '7',
    '######.#.######' : '8',
    '###.##.#.######' : '9',
}

answer = ''     # 답
l = []     # 탐색 상황을 담는 리스트 
cnt = 0     # l 안에 있는 요소의 개수
for s in signal:
    if cnt < 10:
        if cnt == 5 and l.count('.') == 5:     # 공백 세로 1줄일 경우
            l.clear()     # 제거
            l.append(s)
            cnt = 1     # cnt 초기화
        else:     # cnt가 5가 아니면서 공백이 아닐 경우
            l.append(s)     # l에 s 추가 이어가기
            cnt += 1     # cnt 1 증가
    elif cnt == 10:     # 세로 2줄 탐색 완료 시
        if l[5:].count('.') == 5:     # 끝의 5개가 모두 .일 경우
            answer += '1'     # 앞의 세로 한 줄은 1이고 뒤의 세로 한 줄은 공백이므로 answer에 1 추가
            l.clear()     # l비우기
            l.append(s)
            cnt = 1     # cnt 초기화
        else:     # 그렇지 않으면
            l.append(s)     # l에 s 추가 이어나가기
            cnt += 1     # cnt 1 증가
    elif cnt > 10:     # cnt가 0보다 큰 경우 2부터 9까지의 숫자인지를 살펴야 함.
        if ''.join(l) in num:     # 따라서 l을 join한 시그널이 num의 key로 존재하면
            answer += num[''.join(l)]     # answer에 해당 숫자 추가
            l.clear()     # l 비우기
            l.append(s)
            cnt = 1     # cnt 초기화
        else:     # 그렇지 않을 경우
            l.append(s)     # l에 s 추가 이어나가기
            cnt += 1     # cnt 1 증가
if len(l) != 0:
    if ''.join(l) in num:
        answer += num[''.join(l)]
print(answer)