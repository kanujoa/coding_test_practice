p = list(map(int, input().split()))
for i in [1-p[0], 1-p[1], 2-p[2], 2-p[3], 2-p[4], 8-p[5]]:
    print(i, end=' ')

# 다른 방법
# list1 = map(int, input().split())     --> 입력받은 피스의 개수
# list2 = [1, 1, 2, 2, 2, 8]     --> 있어야 하는 흰색 피스의 개수
# a = [y-x for x, y in zip(list1, list2)]     
# --> zip() 함수는 여러 개의 순회 가능한(iterable) 객체를 인자로 받고, 각 객체가 담고 있는 원소를 튜플의 형태로 차례로 접근할 수 있는 반복자(iterator)를 반환
# for i in a:     
#     print(i, end=' ')