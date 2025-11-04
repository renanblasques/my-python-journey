texto = input()
palavra = input()

inicio = 0

while True:
    pos = texto.find(palavra, inicio)
    if pos == -1:
        break
    print(pos)
    inicio = pos + len(palavra)
