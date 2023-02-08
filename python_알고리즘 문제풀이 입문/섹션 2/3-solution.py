n, k = map(int, input().split())     # n과 k 숫자 입력받기
a = list(map(int, input().split()))     # n개의 카드값 입력받기
res = set()     # 중복을 제거하는 자료구조 set!
# 겹치지 않게 카드를 뽑아야 한다! (3장을 한꺼번에 뽑으므로)
for i in range(n):     # 첫번째 자료 뽑기 (인덱스는 0번부터 돌아야 함, 리스트 a의 길이 = n)
  for j in range(i+1, n):     # 두번째 자료 뽑기(첫번째 자료 뒤에 있는 자료들 중에서)
    for m in range(j+1, n):     # 세번째 자료 뽑기(두번째 자료 뒤에 있는 자료들 중에서)
      res.add(a[i] + a[j] + a[m])     # res(set 자료구조)에 넣어 세 수의 합 중 중복 제거하기
# set은 sort메서드 불가, 따라서 내림차순 정렬 위해 list화
res = list(res)    
res.sort(reverse=True)
print(res[k-1])