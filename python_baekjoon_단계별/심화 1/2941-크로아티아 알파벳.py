croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]     # "dz="를 "z="보다 먼저 적어야 한다. 그래야 dz=가 있을 때 dz=를 먼저 탐색하기 때문에 z=로 인식되지 않을 수 있다.
word = input()
for i in croatia:     
    if i in word:     # word에서 crotia 리스트 요소들을 하나씩 다 찾아본 후 있으면
        word = word.replace(i, "a")     # 그 부분을 길이가 1인 문자로 치환한다.    
print(len(word))     # 그리고 바뀐 word의 길이를 구하면 간단하게 끝 ...

# i가 word에 없으면 replace가 일어나지 않고 넘어가기 때문에 if문은 생략해도 된다.