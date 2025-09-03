import random

seed = int(input())
random.seed(seed)

player_points = 0
bank_points = 0
first_decision = True
player_plays = True
bank_plays = True

while player_plays:
    if first_decision:
        decision = "hit"
        first_decision = False
    else:
        decision = input()
    if decision == "hit":
        card_number = random.randint(1, 13)
        if card_number == 1:
            card_name = "A"
        elif card_number == 11:
            card_name = "J"
        elif card_number == 12:
            card_name = "Q"
        elif card_number == 13:
            card_name = "K"
        else:
            card_name = str(card_number)
        if card_number > 10:
            card_number = 10
        player_points += card_number
        print(f"Você tirou {card_name} (total {player_points})")
    if player_points > 21:
        print("Você estourou! Banco vence.")
        bank_plays = False
        player_plays = False
    if decision == "stand":
        print("Você decidiu parar.")
        player_plays = False

while bank_plays:
    if bank_points < 17:
        card_number = random.randint(1, 13)
        if card_number == 1:
            card_name = "A"
        elif card_number == 11:
            card_name = "J"
        elif card_number == 12:
            card_name = "Q"
        elif card_number == 13:
            card_name = "K"
        else:
            card_name = str(card_number)
        if card_number > 10:
            card_number = 10
        bank_points += card_number
        print(f"Banco tirou {card_name} (total {bank_points})")
    if 17 <= bank_points <= 21:
        print("Banco parou.")
        bank_plays = False
    if bank_points > 21:
        print("Banco estourou! Você vence.")
        bank_plays = False

if player_points <= 21 and bank_points <= 21:
    print(f"Você: {player_points}, Banco: {bank_points}")
    if player_points == bank_points:
        print("Empate!")
    elif player_points > bank_points:
        print("Você venceu!")
    else:
        print("Banco venceu!")