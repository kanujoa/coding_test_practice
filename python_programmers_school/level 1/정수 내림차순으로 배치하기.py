def solution(n):
    return int(''.join(sorted([i for i in str(n)], reverse=True)))
# 파이썬에서는 문자형으로 된 숫자에 sorted를 적용해도 숫자일 경우의 오름차순 순서대로 배치됨.
# print(list(str(n)))     --> for문을 쓰지 않고 이렇게 작성해도 숫자 하나하나가 str type으로 리스트의 요소로 담김.
# 근데 sorted를 사용하면 자동으로 리스트에 담긴 결과를 반환하기 때문에 굳이 list를 쓰지 않아도 됨.