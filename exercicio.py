x = (input("Digite seu nome: "))
print("ola",x)

print("opção1")
print("opção2")
print("opção3")

y = int(input("Escolha uma opção: "))

if y == 1:
    v = int(input("Digite um valor: "))
    if v % 2 == 0:
        print("par")
    else:
        print("impar")
elif y == 2:
    n1 = int(input("Digite a primeira nota: "))
    n2 = int(input("Digite a segunda nota: "))
    n3 = int(input("Digite a terceira nota: "))
    media = (n1 + n2 + n3) / 3
    print("media: ", media)
    while media >= 5:
        print("aprovado")
        break
    while media < 5:
        print("reprovado")
        break
elif y == 3:
    exit
else:
    print("opcao invalida")