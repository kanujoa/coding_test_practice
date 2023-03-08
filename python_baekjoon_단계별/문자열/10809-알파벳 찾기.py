s = input()
alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
res = []
for alphabet in alphabets:
    if alphabet in s:
        res.append(str(s.index(alphabet)))
    else:
        res.append("-1") 
print(" ".join(res))

# 아스키 코드와 find 메서드를 이용한 빠른 풀이
# s = input()
# for i in range(97,123):     --> 아스키코드(97부터 122까지)를 문자열로 변환하는 chr() 함수 사용해 a부터 z까지를 s에서 find() 메서드를 이용해 찾는다.
#     print(s.find(chr(i)), end=' ')     --> 한칸씩 띄워서 출력해야 하므로 end=' '도 작성해 주기!
# find() 메서드는 찾으려는 문자가 있을 경우 가장 작은 인덱스값을, 없을 경우에는 -1을 반환한다.