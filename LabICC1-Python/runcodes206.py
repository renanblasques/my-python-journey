sports = int(input())
arts = int(input())
sciences = int(input())

score = 2 * sports + 3 * arts + 5 * sciences

if score >= 200:
    medal = 'O'
elif 150 <= score < 200:
    medal = 'S'
elif 100 <= score < 150:
    medal = 'B'
else:
    medal = 'N'

print(medal)