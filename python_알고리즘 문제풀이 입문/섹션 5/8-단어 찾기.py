n = int(input())
note = []
for _ in range(n):
    note.append(input())
for _ in range(n-1):
    word = input()
    if word in note:
        note.remove(word)
print(note[0])