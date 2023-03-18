def solution(n):
    tenary = ""     # 아래 코드대로 하면 뒤집힌 3진수가 나옴. 따라서 후에 따로 뒤집어줄 필요 X
    while n != 0:
        tenary += str(n % 3)
        n = n // 3
    return int(tenary, 3)     # 3진수를 10진수로 변환하는 코드

# python에 10진수를 2, 8 16진수로 바꿀 수 있는 내장 함수들이 있지만 그 이외의 진수로 바꾸기 위해서는 직접 코드를 작성해야 한다.  