N = int(input())

def front(n):
    if n > N:
        return
    else:
        print(n, end=' ')
        front(n*2)
        print(n, end=' ')
        front(n*2+1)
        print(n, end=' ')
front(1)

# def back(n):
#     if n > 