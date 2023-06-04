n = int(input())
total = n * 2 - 1

for i in range(1, n + 1):
    star = i * 2 - 1
    result = ' ' * ((total - star) // 2) + '*' * star + ' ' * ((total - star) // 2)
    print(result.rstrip())     # 뒷 공백을 없애야 출력 형식이 잘못되었습니다 가 뜨지 않는다.