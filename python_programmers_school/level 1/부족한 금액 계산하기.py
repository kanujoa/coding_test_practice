def solution(price, money, count):
    total_price = price * (count*(count+1) / 2)
    if money - total_price < 0:
        return total_price - money
    return 0

# 한줄 코드
# def solution(price, money, count):
#     return max(0,price*(count+1)*count//2-money)     --> 0과 오른쪽 값 중 더 큰 것을 반환!
# 오른쪽 값이 양수면 돈이 모자르다는 의미이고 0보다 크므로 그 값이 반환된다.
# 오른쪽 값이 음수면 돈이 모자르지 않다는 의미이고 0보다 작으므로 0이 반환된다.