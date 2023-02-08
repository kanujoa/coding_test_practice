'''
람다 함수
'''
'''
def plus_one(x):
    return x+1

print(plus_one(1))
'''
'''
plus_two=lambda x: x+2
print(plus_two(1))
'''
def plus_one(x):
    return x+1

a = [1, 2, 3]
print(list(map(plus_one, a)))     # a라는 리스트의 자료를 plus_one 함수에 적용
# map(함수명, 자료형(or변수))
print(list(map(lambda x: x+1, a)))     # 바로 위 코드와 같은 결과


# 알고리즘 문제를 풀 때는 sort의 인자로 lambda 함수를 사용하여 어떤 것 기준으로 오름차순으로 정리할지를 정함.
