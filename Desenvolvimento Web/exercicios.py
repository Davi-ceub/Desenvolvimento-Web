# Exercicio 1:

# x = input("Digite o seu nome: ")
# y = int(input("Digite sua idade: "))
# z = input("Digite sua cidade: ")

# Usuario = {"nome":x,"idade":y,"cidade":z}
# print(Usuario)

#Exercicio 2:

# List = [1,1,2,3,4,5,5,6,6,6,7,8,8,9]
# List.remove(1)
# List.remove(5)
# List.remove(6)
# List.remove(6)
# List.remove(8)
# print(List)

# #Exercicio 3:
# Lista = [1,1,2,3,4,5,5,6,6,6,7,8,8,9]
# Lista_nova = (set(Lista))
# print(Lista_nova)

# Exercicio 4 :

# Cadastro =[{"Nome":"Joao","Idade":"34","Cargo":"Administrador","Salario":"10000"},
# {"Nome":"Maria","Idade":"45","Cargo":"Secretaria","Salario":"8400"},
# {"Nome":"Pedro","Idade":"29","Cargo":"Faxineiro","Salario":"7500"},
# {"Nome":"Lucas","Idade":"18","Cargo":"Programador","Salario":"2500"},
# {"Nome":"Carlos","Idade":"58","Cargo":"Gerente","Salario":"20000"}
# ]
# print(Cadastro)

#Exercicio 5:

# class Retangulo :
#     def __init__(self,x1,y1,x2,y2):
#         self.base = x2 - x1
#         self.altura = y1 - y2
        

#     def perimetro(self):
#         return self.base*2 + self.altura*2
        

#     def area(self):
#         return self.base * self.altura


#Exercicio 6:
class Pessoa:
    def __init__(self,nome):
        self.nome = nome
    def apresentar(self):
        print("Meu nome é: " + self.nome)

class Funcionario(Pessoa):
    def __init__(self,nome,cargo):
        super().__init__(nome)
        self.cargo = cargo
    
    def apresentar(self):
        print("meu cargo é: " + self.cargo)

Pessoa1 = Pessoa("Davi")
Pessoa2 = Pessoa("Joao","Gerente")
Pessoa1.apresentar()
Pessoa2.apresentar()



