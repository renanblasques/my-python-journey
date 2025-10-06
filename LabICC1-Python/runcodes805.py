def expensive_and_cheap(products: dict) -> tuple:
    expensive = max(products, key=products.get)
    cheap = min(products, key=products.get)
    return expensive, cheap

n = int(input())

products = {}

for _ in range(n):
    name = input().strip()
    price = float(input().strip())
    products[name] = price

print("Lista de compras:")
for name, price in products.items():
    print(f"- {name}: R$ {price:.2f}")

total = sum(products.values())
average = total / len(products)
print(f"\nTotal da compra: R$ {total:.2f}")
print(f"Media de precos: R$ {average:.2f}")

expensive, cheap = expensive_and_cheap(products)
print(f"Mais caro: {expensive} (R$ {products[expensive]:.2f})")
print(f"Mais barato: {cheap} (R$ {products[cheap]:.2f})")

search = input()
if search in products:
    print(f"\nProduto encontrado: {search} custa R$ {products[search]:.2f}")
else:
    print(f"\nProduto nao encontrado: {search}")