import random

# Entrada
S = int(input())
n = int(input())
dist = input().strip()
params = list(map(float, input().split()))

# Inicializa o gerador
random.seed(S)

# Gerar amostras
amostra = []
if dist == "uniforme":
    a, b = params
    for _ in range(n):
        amostra.append(random.uniform(a, b))
elif dist == "binomial":
    N, p = params
    for _ in range(n):
        amostra.append(random.binomialvariate(int(N), p))
elif dist == "beta":
    alpha, beta = params
    for _ in range(n):
        amostra.append(random.betavariate(alpha, beta))
elif dist == "exponencial":
    lambd, = params
    for _ in range(n):
        amostra.append(random.expovariate(lambd))
elif dist == "gamma":
    alpha, beta = params
    for _ in range(n):
        amostra.append(random.gammavariate(alpha, beta))
elif dist == "gauss":
    mu, sigma = params
    for _ in range(n):
        amostra.append(random.gauss(mu, sigma))
elif dist == "lognormal":
    mu, sigma = params
    for _ in range(n):
        amostra.append(random.lognormvariate(mu, sigma))
elif dist == "pareto":
    alpha, = params
    for _ in range(n):
        amostra.append(random.paretovariate(alpha))
elif dist == "weibull":
    alpha, beta = params
    for _ in range(n):
        amostra.append(random.weibullvariate(alpha, beta))

# Estatísticas
def media(x):
    return sum(x)/len(x)

def mediana(x):
    s = sorted(x)
    n = len(s)
    if n % 2 == 1:
        return s[n//2]
    else:
        return (s[n//2 - 1] + s[n//2]) / 2

def quartis(x):
    s = sorted(x)
    n = len(s)
    Q1 = s[n//4]
    Q3 = s[(3*n)//4]
    return Q1, Q3

def desvio_padrao(x):
    m = media(x)
    return (sum((xi - m)**2 for xi in x)/len(x))**(1/2)

def desvio_absoluto_medio(x):
    m = media(x)
    return sum(abs(xi - m) for xi in x)/len(x)

def coef_assimetria(x):
    m = media(x)
    sd = desvio_padrao(x)
    return sum((xi - m)**3 for xi in x)/(len(x)*sd**3) if sd != 0 else 0.0

def coef_curtose(x):
    m = media(x)
    sd = desvio_padrao(x)
    return sum((xi - m)**4 for xi in x)/(len(x)*sd**4) if sd != 0 else 0.0

# Cálculos
m = media(amostra)
med = mediana(amostra)
mn = min(amostra)
mx = max(amostra)
Q1, Q3 = quartis(amostra)
iqr = Q3 - Q1
sd = desvio_padrao(amostra)
var = sd**2
cv = sd/m if m != 0 else 0
dam = desvio_absoluto_medio(amostra)
skew = coef_assimetria(amostra)
kurt = coef_curtose(amostra)

# Saída
print("Média:", round(m,6))
print("Mediana:", round(med,6))
print("Mínimo:", round(mn,6))
print("Máximo:", round(mx,6))
print("Q1:", round(Q1,6))
print("Q3:", round(Q3,6))
print("Amplitude interquartil:", round(iqr,6))
print("Variância:", round(var,6))
print("Desvio padrão:", round(sd,6))
print("Coeficiente de variação:", round(cv,6))
print("Desvio absoluto médio:", round(dam,6))
print("Coeficiente de assimetria:", round(skew,6))
print("Coeficiente de curtose:", round(kurt,6))