from unicodedata import category

weight = float(input())
height = float(input())

imc = weight / (height * height)
imc_class = ""

if imc < 18.5:
    imc_class = "magreza"
elif 18.5 <= imc < 25.0:
    imc_class = "normal"
elif 25 <= imc < 30.0:
    imc_class = "sobrepeso"
elif 30 <= imc < 40:
    imc_class = "obesidade"
elif imc >= 40:
    imc_class = "obesidade grave"
else:
    imc_class = "valor invalido"

print(imc_class)