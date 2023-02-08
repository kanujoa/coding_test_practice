# 최솟값 구하기

arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = float('inf')     # python에서 가장 큰 값(무한)이 저장되게 됨. (가장 큰 값으로 초기화시킨 것)
for i in range(len(arr)):
    if arr[i] < arrMin:     # arr[i]가 arrMin보다 작을 때마다 arrMin에 대입되는 수가 arr[i]로 바뀌게 됨.
        arrMin = arr[i]
print(arrMin)        


# 초기화 시 arr[0] 값으로 설정해도 됨.
arr= [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = arr[0]
for x in arr:
    if x < arrMin:
        arrMin = x
print(arrMin)
