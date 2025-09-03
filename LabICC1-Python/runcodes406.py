numerator_sum = 0
denominator_sum = 0
x_list = []
y_list = []

n_points = int(input())
for i in range(n_points):
    x_list.append(int(input()))
    y_list.append(int(input()))

x_mean = sum(x_list) / n_points
y_mean = sum(y_list) / n_points

for i in range(n_points):
    numerator_sum += (x_list[i] - x_mean) * (y_list[i] - y_mean)
    denominator_sum += (x_list[i] - x_mean) * (x_list[i] - x_mean)

angular_coefficient = numerator_sum / denominator_sum
linear_coefficient = y_mean - angular_coefficient * x_mean

print(f"{angular_coefficient:.2f}")
print(f"{linear_coefficient:.2f}")