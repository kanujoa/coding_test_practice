def solution(numbers):
    numbers.sort()     # sort 메서드는 '행동'에 해당하기 때문에 이것을 그대로 출력하면 None이라고 나온다. 특정 값을 내게 하는 함수가 아니다.
    return numbers[-1] * numbers[-2]     # numbers를 다시 불러주면 sort 메서드가 반영된 상태로 적용되게 된다.(오름차순이 되어있는 numbers로 적용됨.)

# 다른 풀이
# def solution(numbers):
#     return sorted(numbers)[-1] * sorted(numbers)[-2]     --> 다음과 같이 sorted(argument)를 사용하면 한번에 인덱싱이 가능하다.