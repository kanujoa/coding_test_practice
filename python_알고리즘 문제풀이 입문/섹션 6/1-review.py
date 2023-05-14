def binary(n, remain):
    if n == 0:
        print(remain, end='')
    elif n > 0:
        binary(n // 2, n % 2)
        print(remain, end='')

def main():
    n = int(input())
    if n % 2 == 0:
        binary(n // 2, 0)
    else:
        binary(n // 2, 1)

main()