# 콜라츠 추측 함수를 따로 만들었다.
def collatz(num, answer):     # num: 콜라츠 추측을 위한 현재 숫자, answer: 몇 번 반복했는지에 대한 정보
    # 1-1. 입력된 수가 짝수라면 2로 나눈다.
    if num % 2 == 0:
        return collatz(num // 2, answer + 1)     # 다음으로 들어갈 숫자는 2로 나눈 num // 2, 반복 횟수는 1 증가
    # 1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더한다.
    elif num % 2 == 1:     
        return collatz(num * 3 + 1, answer + 1)     # 다음으로 들어갈 숫자는 3을 곱하고 1을 더한 num * 3 + 1, 반복 횟수는 1 증가
    # 2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복한다.
    # 다음 순서로 호출된 함수의 num 인자가 1이면, 콜라츠 추측이 성립한 것이므로 몇 번 반복했는지에 대해 바로 반환하여 함수 호출을 종료한다.
    if num == 1:
        return answer
    # 3. 작업을 500번 반복할 때까지 1이 되지 않는다면 -1을 반환한다.
    if answer == 500:
        return -1
    


def solution(num):
    collatz(num, 0)