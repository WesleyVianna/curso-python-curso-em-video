'''
Desafio 063
Escreva um programa que leia um número N inteiro qualquer e 
mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
Exemplo:
0 – 1 – 1 – 2 – 3 – 5 – 8
'''

print("-" * 38)
print("Sequência de Fibonacci")
print("-" * 38)

n = int(input("Quantos termos você quer mostrar? "))

t1 = 0
t2 = 1

print("~" * 38)
print("{} → {}".format(t1, t2), end=" ")

cont = 3
while cont <= n:
    t3 = t1 + t2
    print(" → {}".format(t3), end=" ")
    t1 = t2
    t2 = t3
    cont += 1

print(" → FIM")
print("~" * 38)