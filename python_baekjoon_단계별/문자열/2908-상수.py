a, b = input().split()
print(a[::-1] if int(a[::-1]) > int(b[::-1]) else b[::-1])

# 더 짧은 풀이
# print(max(input()[::-1].split()))     --> input()에서 reverse 시키고 split()을 하면 두 숫자는 어차피 리스트 형태로 저장됨.
# --> max 함수를 이용해 두 수 중 더 큰 수를 출력함. (int로 형변환 해주지 않아도 정상적으로 작동됨.)