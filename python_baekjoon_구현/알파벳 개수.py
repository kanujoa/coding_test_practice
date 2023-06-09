s = input()
alphabet = {}
for num in range(97, 123):
    alphabet[chr(num)] = 0
for letter in s:
    alphabet[letter] += 1
for item in alphabet.values():
    print(item, end=' ')