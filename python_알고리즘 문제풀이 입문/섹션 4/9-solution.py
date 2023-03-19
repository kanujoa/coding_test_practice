n = int(input())
a = list(map(int, input().split()))
lt = 0
rt = n - 1
last = 0
res = ""     # L과 R을 출력하기 위한 변수
tmp = []     # lt에서의 값(튜플)과 rt에서의 값(튜플)을 넣기 위한 리스트
while lt <= rt:     # lt가 rt와 같아질 때까지만 반복
    if a[lt] > last:     # 마지막 값인 last보다 a[lt]가 크다면 
        tmp.append((a[lt], "L"))     # tmp에 튜플 (a[lt], "L") 추가
    if a[rt] > last:     # 마지막 값인 last보다 a[rt]가 크다면 
        tmp.append((a[rt], "R"))     # tmp에 튜플 (a[rt], "R") 추가
    # 두 튜플 중 더 작은 값을 증가수열의 다음 항으로 적용해야 함.
    tmp.sort()     # 각 튜플의 첫번째 자료(a[lt], a[rt])를 기준으로 오름차순 정렬
    if len(tmp) == 0:     # tmp 리스트에 아무것도 들어 있지 않은 경우 (a[lt]또는 a[rt]값이 last보다 작으면 그것은 tmp에 추가될 수 없다. (애초에 비교 대상이 될 수 없음.))
        break     # 반복문 종료
    else:     # tmp 리스트에 요소가 있을 경우
        res += tmp[0][1]     # tmp 가장 앞 자료의 L / R 부분 res에 추가
        last = tmp[0][0]     # last에 수열에 마지막으로 추가된 숫자를 저장함.
        if tmp[0][1] == "L":     # tmp[0][1]이 L일 경우
            lt += 1     # lt가 증가(이동)
        else:     # tmp[0][1]이 R일 경우
            rt -= 1     # rt가 감소(이동)
    tmp.clear()     # 다음 비교를 위해 tmp 리스트의 요소들을 모두 삭제해 준다.
print(len(res))     # 증가수열의 최대 개수는 가져간 숫자의 방향들을 모아놓은 res의 길이와 같다.
print(res)