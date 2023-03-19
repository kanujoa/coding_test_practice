# 증가수열: 기존의 수열에서 임의의 숫자들을 뽑았을 때 오름차순인 경우를 의미한다. 
# (연속하는 숫자가 아니어도 되고, 이미 뽑은 숫자의 순서를 바꾸는 것은 불가능하다.)
# 실패

n = int(input())
seq = list(map(int, input().split()))
cur = 0
res1 = ""
res2 = ""
lt = 0
rt = n-1
while lt < rt:
    if seq[lt] < seq[rt]:
        if seq[lt] > cur:
          cur = seq[lt]
          res1 += str(cur)
          res2 += "L"
          lt += 1
        else:
            if seq[rt] > cur:
                cur = seq[rt]
                res1 += str(cur)
                res2 += "R"
            rt -= 1
    elif seq[rt] < seq[lt]:
        if seq[rt] > cur:
            cur = seq[rt]
            res1 += str(cur)
            res2 += "R"
            rt -= 1
        else:
            if seq[lt] > cur:
                cur = seq[lt]
                res1 += str(cur)
                res2 += "L"
            rt -= 1
print(len(res1))
print(res2)