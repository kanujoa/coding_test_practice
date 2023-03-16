n = int(input())
cnt = 0
for _ in range(n):
    word = input()
    prev = ""
    cur = word[0]
    for i in word:
        if i != cur:
            prev += cur
            cur = i
            if cur in prev:
                break
    else:
        cnt += 1
print(cnt)        

# 간단한 코드
# def g(a): return list(a)==sorted(a,key=a.find)
# print(sum(g(input()) for _ in range(int(input()))))