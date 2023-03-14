def solution(d, budget):
    d.sort()     # 애초에 오름차순 정렬을 해버리면 작은 값들부터 더해나가기 때문에 최대로 지원해줄 수 있는 경우를 여러 경우의 수를 살피지 않고 구할 수 있다.
    s = 0     # 신청 금액을 더한 값을 저장할 변수
    cnt = 0     # 지원해줄 수 있는 팀의 수룰 저장할 변수
    for i in d:     # 적은 금액을 신청한 팀부터 탐색
        s += i     
        cnt += 1
        if s > budget:     # 신청 금액 합이 예산보다 커질 경우
            return cnt - 1     # cnt-1 값 반환하고 끝 (앞에서 불가능한 경우에 cnt+1을 해주었으므로 그거 되돌리기 위해)
    else:     # 신청 금액 합이 예산보다 작거나 같아서 위 for문을 그냥 빠져나온 경우
        return len(d)     # 모든 팀에 지원 가능하므로 배열 d의 길이 반환

print(solution([1,3,2,5,4], 9))

# 살짝 더 간단한 풀이 (합한 값을 저장하는 변수 사용 X)
# def solution(d, budget):
#     d.sort()
#     cnt = 0
#     for i in d :
#         budget -= i     --> budget에서 신청 금액만큼 빼는 방법을 이용!
#         if budget < 0 :     --> budget이 0보다 작아질 때
#                break     --> 반복문 종료
#         cnt += 1     --> break가 안걸리면 cnt 1 증가
#     answer = cnt
#     return answer