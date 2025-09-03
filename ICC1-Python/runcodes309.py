n = input()

if len(n) != 3 or not n.isdigit():
    exit()

print(n[::-1])