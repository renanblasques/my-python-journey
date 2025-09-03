number = int(input())
if number > 0:
    if number % 2 == 0:
        print("O número é positivo e par.")
    else:
        print("O número é positivo e ímpar.")
elif number == 0:
    print("O número é zero.")
else:
    print("O número é negativo.")