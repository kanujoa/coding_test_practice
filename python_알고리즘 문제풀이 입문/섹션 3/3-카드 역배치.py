cards = [i for i in range(21)]     # 21개의 요소가 있는 리스트 생성. 각 요소의 숫자는 각 인덱스 번호와 일치함.

for i in range(10):     # 구간은 총 10개가 입력되어야 하므로 range(10)을 작성
  section = list(map(int, input().split()))     # 구간을 입력받아 리스트로 만듦. (여기서 구조분해할당을 이용하면 코드 길이를 더 줄일 수 있음.)
  a = section[0]     # section 리스트의 첫번째 요소는 a
  b = section[1]     # section 리스트의 두번째 요소는 b
  for j in range((b - a + 1) // 2):     # 인덱스 번호를 조절할 j의 범위
    cards[a + j], cards[b - j] = cards[b - j], cards[a + j]     # 구간의 가운데를 중심으로 양끝의 카드 번호를 교환함.
cards.remove(0)     # 리스트의 요소 중 0은 필요 없으므로 없애줌. (인덱스때문에 헷갈리지 않게 편의상 만들어 둔 것임.)
for card in cards:
  print(card, end= " ")