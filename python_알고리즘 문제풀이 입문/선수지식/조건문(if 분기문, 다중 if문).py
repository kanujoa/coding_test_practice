'''
조건문 if (분기, 중첩)
'''
'''
x = 5
if x != 7:
    print("Lucky")
    print("ㅋㅋㅋ")
'''
'''
x = 9
if x >= 10:
    if x%2 == 1:
        print("10 이상의 홀수")
'''
'''
x = 10
if x > 0:
    if x < 10:
        print("10보다 작은 자연수")
'''
'''
x = 7
if x > 0  and x < 10:
    print("10보다 작은 자연수")
'''
'''
x = 7
if 0 < x < 10:
    print("10보다 작은 자연수")
'''
'''
x = 10
if x > 0:
    print("양수")
else:
    print("양수")
'''
'''
x = 75
if x >= 90:     # 참이 걸리는 순간 출력하고 끝남. 아래로 가지 않음. (하나의 문장 구조에서)
    print('A')
elif x >= 80:
    print('B')
elif x >= 70:
    print("C")
elif x >= 60:
    print("D")
else:
    print("F")
'''

x = 93
if x >= 90:     # 다중 if의 경우 모두 다른 문장 구조 
    print("A")
if x >= 80:
    print("B")
if x >= 70:
    print("C")
