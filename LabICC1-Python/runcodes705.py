sentence = input()
size = len(sentence)
i = 0

while i < size:
    count = 1
    while i + 1 < size and sentence[i] == sentence[i + 1]:
        count += 1
        i += 1
    if count > 1:
        print(sentence[i] + str(count), end="")
    else:
        print(sentence[i], end="")
    i += 1

print()