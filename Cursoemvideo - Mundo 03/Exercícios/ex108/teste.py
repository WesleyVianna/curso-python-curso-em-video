import moeda

print("-" * 35)
p = float(input("Digite o preço: R$ "))
print("-" * 35)
print(f"A medade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}")
print(f"O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}")
print(f"Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}")
print("-" * 35)