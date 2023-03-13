n = int(input())
length = 2 * n - 1     # 별 찍기 최대 길이
s = 1     # 찍을 별의 개수
while s <= length:
    print(('*' * s).center((length)))     
    s += 2
# center 함수 안에 원하는 문자열의 길이를 넣어주면 알아서 문자는 가운데로, 나머지 부분은 공백으로 채워준다.
while True:
    s -= 2
    if s < 1:     # 마지막에 공백이 출력되면 안된다.
        break
    print(('*' * s).center((length)))   
    
      