def solution(order):
    order = str(order)
    return order.count("3") + order.count("6") + order.count("9")

# 다른 풀이 (lambda 사용)
# def solution(order):
#     return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))
# map 함수: map(function, iterable) (iterable: 리스트, 튜플 등 반복 가능한 자료형), 두 번째로 들어온 자료형의 요소들을 하나씩 함수의 인자로 집어넣는 함수
