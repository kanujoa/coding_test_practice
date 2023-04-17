def solution(num):
    if num % 2:     # 2로 나눈 나머지가 0이 아닌 경우(True) (1인 경우)
        return "Odd"     # 홀수, return 되었으므로 함수 끝남.
    return "Even"     # 나머지가 0인 경우(False) 짝수

# js에서는 음수의 나머지는 음수로 나오는데, python에서는 음수의 나머지도 양수로 나온다.
# [js] 
# console.log(-5 % 2)     --> -1
# console.log(-4 % 2)     --> -0
# [python]
# print(-5 % 2)     --> 1
# print(-4 % 2)     --> 0