age = int(input())
monthly_income = float(input())
purchases_per_year = float(input())
registered_time = float(input())
satisfaction_score = float(input())

if (age < 0 or monthly_income < 0 or purchases_per_year < 0 or registered_time < 0 or 
    satisfaction_score < 0 or satisfaction_score > 100):
    print("Erro: dados de entrada invalidos")
elif satisfaction_score >= 90 and purchases_per_year >= 20000:
    print("VIP")
elif monthly_income >= 10000 or (purchases_per_year > 10000 and registered_time >= 3):
    print("Alto Potencial")
elif age >= 25 and age <= 60 and satisfaction_score >= 50:
    print("Regular")
else:
    print("Baixa Prioridade")