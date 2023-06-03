A = int(input())
B = int(input())
C = int(input())

mul = str(A * B * C)     # 여기에 A, B, C 자리에 int(input())을 넣어 변수에 담지 않고 더 간단하게 코드를 작성해도 된다.

for i in range(0, 10):
    print(mul.count(str(i)))