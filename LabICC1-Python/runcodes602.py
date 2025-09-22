import numpy as np

data = []

while True:
    line = input()
    if line.strip() == "-1":
        break

    parts = line.strip().split()
    name = parts[0]
    scores = list(map(float, parts[1:]))
    data.append([name] + scores)

matrix = np.array(data)
print("Matriz de notas:")
print(matrix)

scores_only = matrix[:, 1:].astype(float)
averages = np.mean(scores_only, axis=1)

index_highest = np.argmax(averages)
name_highest = matrix[index_highest, 0]
highest_average = averages[index_highest]

print(f"\nMaior média: {highest_average:.2f} ({name_highest})")