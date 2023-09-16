#Escreva um programa que calcule a soma de três variáveis e imprima o resultado na tela.

from random import randint

a = randint(1,100)
b = randint(1,100)
c = randint(1,100)
r = a+b+c

print(f'{a} + {b} + {c} = {r}')