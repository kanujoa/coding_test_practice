scale =list( map(int, input().split()))

result = set()
for i in range(1, len(scale)):
    if scale[i-1] < scale[i]:
        result.add('ascending')
    elif scale[i-1] > scale[i]:
        result.add('descending')
if len(result) == 1:
    print(list(result)[0])     # set에서는 인덱싱 불가
else:
    print('mixed')

# 다른 풀이
scale =list(map(int, input().split()))

if scale == [1, 2, 3, 4, 5, 6, 7, 8]:
    print('ascending')
elif scale == [8, 7, 6, 5, 4, 3, 2, 1]:
    print('descending')
else:
    print('mixed')