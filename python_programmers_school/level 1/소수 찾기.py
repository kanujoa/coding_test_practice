def solution(n):
    cnt = [0] * (n + 1)
    for i in range(2, n+1):
        for j in range(1, n//i + 1):
            cnt[i*j] += 1
    return cnt.count(1)

# 다른 풀이
# def solution(n):
#     num=set(range(2,n+1))     --> 2부터 n까지의 수를 집합으로 정의

#     for i in range(2,n+1):     --> i는 2부터 n까지의 수 (i는 곧 소수이다.)
#         if i in num:     --> i가 num에 있다면
#             num-=set(range(2*i,n+1,i))     --> num에서 i의 배수의 집합을 제거함.(집합의 연산 사용, 배수는 range를 사용해 구현)
#     return len(num)     --> 답은 남은 요소들인 소수의 개수를 집합 num의 길이로 구함.