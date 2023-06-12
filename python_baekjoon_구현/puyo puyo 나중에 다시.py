field = [[i for i in input()] for _ in range(12)]
print(field)

def search(color):     # 해당 뿌요의 좌, 우, 아래를 살펴 해당 부분에 뿌요가 있는지 확인하기
    color

for i in range(12):
    if field[i].count('.') != 6:
        for j in range(6):
            if field[i][j] != '.':
                color = field[i][j]
