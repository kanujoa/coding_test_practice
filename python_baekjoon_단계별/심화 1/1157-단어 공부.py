word = input().upper()
alphabets = list(set(word))
cnt = 0
alphabet = ""
for i in alphabets:
    if word.count(i) > cnt:
        cnt = word.count(i)
        alphabet = i
    elif word.count(i) == cnt:     # 이 조건에 닿을 때 바로 print("?")하고 break 하여 끝내버리면 cnt가 최댓값이 아닐 때임에도 불구하고 종료되기 때문에 틀린 코드가 된다.
        alphabet += i     # 따라서 위 조건에서는 우선 alphabet에 현재 i를 추가해 준 후     
if len(alphabet) > 1:     # alphabet에 저장된 문자열의 길이가 2 이상이면 가장 많이 사용된 알파벳이 2개 이상 존재하는 것이므로
    print("?")     # 이때 "?"을 출력
else:     # 아닐 경우 주어진 입력 조건에서는 문자열의 길이가 1인 경우이므로
    print(alphabet)     # alphabet에 저장된 길이 1의 문자를 출력
# 반례는 hifriends에서 찾음.

# 더 간단한 풀이 (chr 이용)
# str = input().upper()
# max_num = 0
# for i in range(26):     # 65부터 90까지가 A~Z까지 해당  
#     cnt = str.count(chr(i + 65))
#     if max_num < cnt:
#         max_num = cnt
#         max_char = chr(i + 65)
#     elif max_num == cnt:
#         max_char = "?"     # 주목! max_num과 cnt가 같을 경우에 max_char에 아예 "?"문자를 대입해 주었다.
# print(max_char)
# 내 방법에서 alphabet += i를 하지 않고 alphabet = "?"로 했으면 마지막에 len(alphabet)을 확인하는 코드를 적지 않아도 바로 print(alphabet)으로 답을 구할 수 있었다.