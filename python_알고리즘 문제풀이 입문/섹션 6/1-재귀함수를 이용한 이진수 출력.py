def transform(num, res):
    if num != 0:
        transform(num // 2, res)
        res += str(num % 2)
    print(res, end='')

N = int(input())
transform(N, "")