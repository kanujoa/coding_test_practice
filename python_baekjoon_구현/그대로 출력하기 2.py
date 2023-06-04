while True:
    try:
        _input = input()
        print(_input)
    except:     # 오류가 나면 반복문을 빠져나가게 하는 코드, VScode에서는 작동을 안하지만 백준에서는 맞게 처리 (EOF --> 입력 끝날때까지 출력하기)
        break