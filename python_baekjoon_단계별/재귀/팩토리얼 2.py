n = int(input())

def DFS(num):
    if num == 1:
        return 1
    else:
        return DFS(num - 1) * num

if n == 0:
    print(1)
else:
    print(DFS(n))
    

# 아래와 같이 작성하면 n이 0인 경우도 한번에 해결 가능
# https://my-coding-notes.tistory.com/670
def fac(num, n):
    if n == 0:
        print(num)
        return

    fac(num*n, n-1)

n = int(input())
fac(1, n)


# 반복문으로 작성하기
n = int(input())
answer = 1    

while n > 0:
    answer *= n
    n -= 1

print(answer)