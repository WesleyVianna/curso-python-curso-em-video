a = (2, 5, 4)
b = (5, 8, 1, 2)

c = b + a

print("=-" * 10)
print(c) # Imprime a tupla c, que contém todos os elementos de b seguidos por todos os elementos de a
print("=-" * 10)
print(len(c)) # Imprime o comprimento da tupla c, ou seja, o número total de elementos em c
print("=-" * 5)
print(c.count(5)) # Imprime o número de ocorrências do elemento 5 na tupla c
print("=-" * 5)
print(c.count(4)) # Imprime o número de ocorrências do elemento 4 na tupla c
print("=-" * 5)
print(c.index(2)) # Imprime o índice da primeira ocorrência do elemento 2 na tupla c
print("=-" * 5)
print(c.index(2, 4)) # Imprime o índice da primeira ocorrência do elemento 2 a partir do índice 4 na tupla c
print("=-" * 5)