alphabet = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
res = 0
for i in input():
    for x in alphabet:
        if i in x:
            res += alphabet.index(x) + 3
print(res)

# 알파벳이 S인 경우와 Z인 경우 예외처리하고 나머지 경우에 규칙을 이용하는 방법을 사용할 수 있음.
# a=0
# l='33344455566677788889990000'           # ABC:3, DEF:4, GHI:5, JKL:6, MNO:7, PQRS:8, TUV:9, WXYZ:0 (적힌 숫자보다 1초씩 더 걸리므로 1을 더한 값으로 적용!)
# for i in input():
#     i=int(l[ord(i)-ord('A')])          # ord('A')는 65다. 
#     if i:a+=i          # i가 0이 아니어서 True일 경우(i가 W, X, Y, Z가 아닐 경우)
#     else:a+=10         # i가 W, X, Y, Z 중 하나인 경우
# print(a)