import moeda

print("-" * 35)
p = float(input("Digite o preço: R$ "))
print("-" * 35)
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(p, 13, True)}')
print("-" * 35)