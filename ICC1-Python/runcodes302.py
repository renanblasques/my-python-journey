salary = float(input())

if salary <= 2500:
    new_salary = salary * 1.20
else:
    new_salary = salary * 1.15

print(f"{new_salary:.2f}")