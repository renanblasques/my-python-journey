leds_per_digit = {
    '0': 6, '1': 2, '2': 5, '3': 5, '4': 4,
    '5': 5, '6': 6, '7': 3, '8': 7, '9': 6
}

n = int(input())

for _ in range(n):
    total_leds = 5
    number = input().strip()
    for digit in number:
        number_of_leds = leds_per_digit[digit]
        total_leds += number_of_leds
    print(f"{total_leds} leds")