num = int(input())
cur = -1
cnt = 0

while cur != num:
    if num < 10:
        num = int(str(num) + '0')
    if cnt == 0:
        cur = num
    right = str(cur)[-1]
    s = sum(map(int, list(n for n in str(cur))))
    cur = int(right + str(s)[-1])
    cnt += 1
print(cnt)

# 다른 풀이 (// 와 %를 사용하면 더 깔끔하게 풀 수 있다!)
N = int(input())
a = N//10     # 주어진 숫자의 왼쪽 자리의 수 (애초에 숫자 범위가 0 이상 99 이하이므로 이렇게 a, b로만 구해도 된다.)
b = N%10     # 주어진 숫자의 오른쪽 자리의 수
i=0     # 카운터 변수

while True:
    c = b*10 + (a+b)%10     # c는 원래 수의 1의 자리와 합으로 나온 수의 1의 자리를 더해서 만들어진다.
    a = c//10     # 위 과정 반복
    b = c%10
    i+=1     # 카운터 증가
    if c==N:     # 각 자리 수의 합과 처음 주어진 숫자가 같아지면 반복문 종료
        break
    else:
        continue
print(i)     # 결과로 카운터 출력