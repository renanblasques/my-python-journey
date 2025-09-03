import random

seed = int(input())
random.seed(seed)

secret_number = random.randint(1, 100)
guessed = False
attempts = 0

while (attempts < 7):
    number = int(input())
    attempts += 1
    if number == secret_number:
        print("Parabéns! Você acertou!")
        break
    if number > secret_number:
        print("O número secreto é menor!")
        continue
    if number < secret_number:
        print("O número secreto é maior!")
else:
    print(f"Suas 7 tentativas acabaram. O número secreto era {secret_number}.")