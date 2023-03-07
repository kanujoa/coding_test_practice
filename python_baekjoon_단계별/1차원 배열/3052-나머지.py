r = [int(input())%42 for _ in range(10)]     # 나머지로만 이루어진 리스트 생성
r = list(set(r))     # 서로 다른 값이 몇 개 있는지를 구하는 것이므로 중복 제거
print(len(r))     # 개수는 len() 함수를 이용해 구하기

# 이렇게 한줄로 적어주면 더 빠르다.
# print(len(set([int(input()) % 42 for _ in range(10)])))