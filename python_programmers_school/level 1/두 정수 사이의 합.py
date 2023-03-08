def solution(a, b):
    big = max([a, b])
    small = min([a, b])
    return sum([i for i in range(small, big+1)])

# 다른 풀이 1 (수학 공식 이용)
# def adder(a, b):
#     return (abs(a-b)+1)*(a+b)//2     --> a-b가 음수일지 양수일지 모르니 abs()로 절댓값으로 만들어 줌

# 다른 풀이 2
# def adder(a, b):
#     if a > b:     --> a, b 순서로 범위를 정해줄 것인데 만약 a가 b보다 큰 상황이 있다면
#         a, b = b, a     --> a와 b를 서로 치환
#     return sum(range(a, b + 1))     --> a이상 b 이하의 수들을 sum으로 모두 더함. (나처럼 리스트에 넣어줄 필요 없이 그냥 range 함수만 사용해도 된다.)

