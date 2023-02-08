n, k = map(int, input().split())
cards = list(map(int, input().split()))

pick = []
# 카드를 세 장 고르는 모든 경우의 수
for a in range(len(cards)):
  for b in range(a+1, len(cards)):
    for c in range(b+1, len(cards)):
      pick.append(cards[a] + cards[b] + cards[c])     # sum 함수는 최대 2개의 인수를 받는다. 따라서 사용 불가능

# 중복 먼저 없애고 리스트로 변환하여 내림차순으로 변환하였다.
pick = list(set(pick))     # 중복 없애기
pick.sort(reverse=True)     # set에서는 sort를 사용할 수 없다. list에서 오름차순 정리해야함. 또한 set은 순서가 없어 인덱스 사용 불가능
print(pick[k-1])