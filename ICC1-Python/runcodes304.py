value = float(input())

int_part = int(value // 1)
decimal_part = value - int_part

print(f"{int_part} + {decimal_part:.2f}")