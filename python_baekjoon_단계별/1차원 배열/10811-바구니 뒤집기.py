n, m = map(int, input().split())
basket = [i for i in range(n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    for x in range((j-i+1)//2):     
        basket[i+x], basket[j-x] = basket[j-x], basket[i+x]
basket.pop(0)
print(" ".join(map(str, basket)))