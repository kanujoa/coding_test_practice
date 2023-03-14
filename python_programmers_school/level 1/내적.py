def solution(a, b):
    return sum(a*b for a, b in zip(a, b))     # zip 사용 시 list로 변환하지 않고 바로 sum 해줘도 가능