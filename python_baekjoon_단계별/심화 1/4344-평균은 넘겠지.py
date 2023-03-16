import sys
input = sys.stdin.readline
c = int(input())
for _ in range(c):
    a = list(map(int, input().split()))
    students = a[0]
    scores = a[1:len(a)]     # len(a)를 안적어줘도 1부터 끝까지 scores에 저장됨
    average = sum(scores) / students
    up = 0
    for score in scores:
        if score > average:
            up += 1
    print(f'{up / students * 100:.3f}%')     # print()와 반올림을 같이 쓰려면 round를 사용하면 안되고 옆과 같이 해야 한다.
# print("{:.3f}%".format(count/m*100))     --> 옆과 같이 적어줄 수도 있음.