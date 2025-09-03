import math

z = float(input())
n = int(input())

delta_x = z/n
soma = 0.0

for k in range(n):
    x = (k * delta_x) + delta_x/2.0

    altura_i = (1.0/math.sqrt(2.0*math.pi) ) * math.exp( - (x*x)/2.0 )
    
    area_i = altura_i * delta_x
    soma += area_i

print(f"{soma:.4f}")