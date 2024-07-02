import moeda

print("-" * 30)
p = float(input("Digite o preço: R$ "))
print("-" * 30)
print(f"A medade de R${p} é R${moeda.metade(p)}")
print(f"O dobro de R${p} é R${moeda.dobro(p)}")
print(f"Aumentando 10%, temos R${moeda.aumentar(p, 10)}")
print("-" * 30)