# PRIMEIRO EXEMPLO

cont = 1

while cont <= 10:
    print(cont, "→ ", end=" ")
    cont += 1
print("Acabou")

# SEGUNDO EXEMPLO

n  = 0 

while n != 999:
    n = int(input("Digite um número: "))

# TERCEIRO EXEMPLO

n = s = 0

while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n

# print("A soma vale {}".format(s))
print(f"A soma vale {s}")
