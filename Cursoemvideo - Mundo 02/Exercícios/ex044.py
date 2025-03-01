'''
Desafio 044
Elabora um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
e condição de pagamento:
- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de descono
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''

print("{:=^40}".format(" LOJAS GUANABARA "))
preco = int(input("Digite o preço das compras: R$ "))

print("""FORMAS DE PAGAMENTO:
    [ 1 ] à vista dinheiro/cheque 
    [ 2 ] à vista cartão
    [ 3 ] 2x no cartão
    [ 4 ] 3x ou mais no cartão""")
opcao = int(input("Digite a sua opção: "))

if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print("Sua compra será parcelada em 2x de R$ {:.2f} SEM JUROS".format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input("Quantas parcelas? "))
    parcela = total / totparc
    print("Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS".format(totparc, parcela))
else: 
    total = preco
    print("OPÇÃO INVÁLIDA de pagamento. Tente novamente!")
print("Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.".format(preco, total))
