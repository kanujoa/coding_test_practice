def solution(cipher, code):
    result = []
    for i in range(len(cipher)):     # 범위 잘 확인해주기
        if (i+1) % code == 0:     # 여기도
            result.append(cipher[i])
    return "".join(result)

# 간단한 풀이 (문자열 슬라이싱 이용)
# def solution(cipher, code):
#     return cipher[code-1::code]    인덱싱할때 0부터 시작하므로 시작은 [code-1], 문자열의 끝까지 볼 것이므로 중앙에는 아무것도 적지 않아도 됨.
#                                    간격은 code의 값만큼(code의 배수만 해당이므로 code만큼 더해주어야 함.)이므로 마지막에는 code를 적어줌.