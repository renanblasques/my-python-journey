income = float(input())
debts = float(input())
loan_amount_request = float(input())

if income <= 0:
    print("renda invalida")
else:
    debt_ratio = debts / income
    if debt_ratio > 1.0:
        loan_response = "negado"
    elif loan_amount_request > 20 * income:
        loan_response = "negado"
    elif 0.5 <= debt_ratio <= 1.0:
        loan_response = "analise manual"
    elif loan_amount_request <= 10 * income and debt_ratio < 0.5:
        loan_response = "aprovado"
    elif 10 * income <= loan_amount_request <= 20 * income and debt_ratio < 0.5:
        loan_response = "analise manual"

print(loan_response)