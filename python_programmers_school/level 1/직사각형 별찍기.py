a, b = map(int, input().strip().split(' '))
for _ in range(b):
    print("*" * a)

# 다른 풀이
# a, b = map(int, input().strip().split(' '))
# answer = ('*'*a +'\n')*b     --> +'\n'을 해줌으로써 for문을 사용해 print를 여러번 해주지 않아도 된다.
# print(answer)