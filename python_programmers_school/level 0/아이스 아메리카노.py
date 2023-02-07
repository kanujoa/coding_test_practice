def solution(money):
    return [money//5500, money-(money//5500*5500)]     # money % 5500 을 하면 잔돈값이 된다.