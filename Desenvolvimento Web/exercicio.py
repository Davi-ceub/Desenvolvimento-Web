x = (input("digite o seu nome:"))
print(x)
y = int(input("digite um numero: "))
if y % 2 == 0:
    print("par")
else :
    print("impar") 


n1 = int(input("digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))
n3 = int(input("digite a terceira nota: "))
media = (n1 + n2 + n3)/3
print(media)
while media > 5:
    print("aprovado")
    break
else :
    print("reprovado")