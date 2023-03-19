from itertools import combinations

n, m = map(int, input().split())      # n: 숫자, m: 제거해야 할 자릿수의 개수
n = [i for i in str(n)]      # n은 str(n)의 한자 한자를 요소로 가지는 리스트로 변경
a = len(n) - m     # a: 제거 후 남는 자릿수의 개수

cur = 0
for i in list(combinations(n, a)):
    if int("".join(list(i))) > cur:
        cur = int("".join(list(i)))
print(cur)

# 답은 맞지만 입력 숫자가 길어지면 시간 초과됨.