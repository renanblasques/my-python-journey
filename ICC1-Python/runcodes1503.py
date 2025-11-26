cpf = input().strip()
cpf = cpf.replace('-', '').replace('.', '')

s1 = 0
s2 = 0
d10 = 0
d11 = 0

for i in range(0, 9):
    s1 += (10 - i) * int(cpf[i])

if s1 % 11 < 2:
    d10 = 0
else:
    d10 = 11 - (s1 % 11)

for i in range(0, 10):
    s2 += (11 - i) * int(cpf[i])

if s2 % 11 < 2:
    d11 = 0
else:
    d11 = 11 - (s2 % 11)

if d10 == int(cpf[9]) and d11 == int(cpf[10]):
    print("CPF valido")
else:
    print("CPF invalido")