def solution(n):
    watermelon = []
    for i in range(1, n+1):
        if i % 2 == 0:     # 짝수번째일때는 "박"
            watermelon.append("박")
        else:     # 홀수번째일때는 "수"가 들어가야 함
            watermelon.append("수")
    return "".join(watermelon)     # 마지막에 리스트 요소들 공백 없이 합쳐줌

# 다른 풀이 
# def water_melon(n):
#     return "수박" * (n//2) + "수" * (n%2)     --> n이 짝수면 끝이 (수)박으로 끝나고 n이 홀수면 끝이 수로 끝난다.

# 다른 풀이 2
# def solution(n):
#     return "".join(["수박"[i%2] for i in range(n)])     --> i 0부터 시작("수"부터 시작), i 홀수일 때(n에서는 짝수) "박", i 짝수일 때(n에서는 홀수) "수"