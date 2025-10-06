password = input()
valid_password = True

if len(password) < 6 or len(password) > 20:
    print("senha fraca: tamanho invalido")
    valid_password = False

if password.isupper():
    print("senha fraca: sem minuscula")
    valid_password = False

if password.islower():
    print("senha fraca: sem maiuscula")
    valid_password = False

if password.isalpha():
    print("senha fraca: sem digito")
    valid_password = False

if not password.isascii():
    print("senha fraca: caracteres invalidos")
    valid_password = False

count = 1
for i in range(len(password) - 1):
    if password[i] == password[i + 1]:
        count = count + 1
    else:
        count = 1
    if count > 2:
        print(f"senha fraca: {count} caracteres repetidos")
        valid_password = False
        break

found_date = False
for i in range(len(password)):
    for length in (6, 8):
        if i + length <= len(password):
            s = password[i:i+length]
            if s.isdigit():
                day = int(s[0:2])
                month = int(s[2:4])

                if length == 6:
                    year = int(s[4:6])
                    if 0 <= year <= 25:
                        year += 2000
                    else:
                        continue
                else:
                    year = int(s[4:8])
                    if not (1900 <= year <= 2025):
                        continue

                
                bissexto = False
                if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
                    bissexto = True

                
                if month == 2:
                    max_day = 29 if bissexto else 28
                elif month in (1, 3, 5, 7, 8, 10, 12):
                    max_day = 31
                elif month in (4, 6, 9, 11):
                    max_day = 30
                else:
                    continue

                
                if 1 <= day <= max_day:
                    print("senha fraca: data valida")
                    valid_password = False
                    found_date = True
                    break
    if found_date:
        break

if (valid_password):
    print("senha forte")