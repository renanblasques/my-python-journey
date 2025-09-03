import math

n_points = int(input())
total_distance = 0.0
coords_list = []

for i in range(n_points):
    str_coords = input()
    int_coords = list(map(int, str_coords.split()))
    coords_list.append([int_coords[0], int_coords[1]])

for i in range(n_points - 1):
    x1 = coords_list[i][0]
    x2 = coords_list[i + 1][0]
    y1 = coords_list[i][1]
    y2 = coords_list[i + 1][1]
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    total_distance += distance

print(f"{total_distance:.4f}")