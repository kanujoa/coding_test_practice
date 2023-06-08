# 정답에는 키를 넣어야 한다. (taller[i][0] == 키, taller[i][1] == 자기보다 큰 사람의 수)
n = int(input())     # 사람의 수 
taller = list(enumerate(map(int, input().split())))
taller.sort(key=lambda x:(x[1], -x[0]))     # 키가 큰 사람의 수 기준으로 오름차순 정렬하되, 그 수가 같으면 키를 기준으로 내림차순 정렬
answer = []

for i in range(len(taller)):
    if i == 0:
        answer.append(taller[i])     
    else:
        cnt = taller[i][1]
        if cnt == 0:
            answer.insert(0, taller[i])     # list.insert(index, 넣을 문자)
        else:
            for j in range(len(answer)):
                if answer[j][0] > taller[i][0]:
                    cnt -= 1
                    if cnt == 0:
                        answer.insert(j+1, taller[i])
                        break

for a in answer:
    print(a[0] + 1, end=' ')