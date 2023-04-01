# 내 풀이와 비슷

a = input()
b = input()
sH = dict()
for x in a:
    sH[x] = sH.get(x, 0) + 1
for x in b:
    sH[x] = sH.get(x, 0) - 1
for x in a:     # a 문자열에 있는 문자들(key)의 값이 0이 아니라면 문자열 b에서 a와 일치하지 않는 문자가 있거나 개수가 일치하지 않았다는 의미임.
    if sH.get(x) > 0:
        print("NO")     # 따라서 NO 출력하고 종료
        break
else:
    print("YES")