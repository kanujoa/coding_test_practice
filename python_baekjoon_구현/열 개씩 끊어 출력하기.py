word = input()

i = 0
for _ in range(len(word) // 10):
    print(word[i : i + 10])
    i += 10
print(word[i:])