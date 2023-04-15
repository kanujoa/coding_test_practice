def new_num(x):     # 이걸 해주지 않고 그냥 아래에서 한번에 a = (a + 1) // 2, b = (b + 1) // 2 이렇게 해주면 된다. 
    if x % 2 == 0:
        return x // 2
    else:
        return (x + 1) // 2

def solution(n,a,b):
    match = 1
    bind = [(i, i+1) for i in range(1, n, 2)]
    while True:
        if (a, b) in bind or (b, a) in bind:
            return match
        match += 1
        a = new_num(a)
        b = new_num(b)


# 간단한 풀이
def solution(n,a,b):
    answer = 0
    while a != b:     # a와 b가 같아질 때까지 반복
        answer += 1
        a, b = (a+1)//2, (b+1)//2

    return answer

print(solution(8, 4, 7))