#Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto. 
#Considere que pagam imposto pessoas cujo salário é maior que R$ 1.200,00.

def imposto():
        salario = float(input('Digite seu salário: R$ '))
        if salario > 1200:
            return "Você vai pagar imposto"
        else:
            print("Você não prrecisa pagar imposto")

print(imposto())
