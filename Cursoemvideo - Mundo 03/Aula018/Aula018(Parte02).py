galera = [["João", 19], ["Ana", 33], ["Joaquim", 13], ["Maria", 45]]

print(galera[0][0])
print(galera[2][1])

print("--------------------")

for p in galera:
    print(p)

print("--------------------")

for p in galera:
    print(f"{p[0]} tem {p[1]} anos de idade.")