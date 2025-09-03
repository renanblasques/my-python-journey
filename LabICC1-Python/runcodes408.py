mat = [[],[],[]]

for i in range(3):
    for j in range(3):
        mat[i].append(int(input()))

max_num = mat[0][0]

for i in range(3):
    for j in range(3):
        if mat[i][j] > max_num:
            max_num = mat[i][j]

for i in range(3):
    for j in range(3):
        if mat[i][j] == max_num:
            mat[i][j] = -1

for i in mat:
    print(*i)