''' Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado. Para ser aprovado, todas as médias do aluno devem ser 
maiores que 7. Considere que o aluno cursa apenas três matérias, e que a nota de cada uma está armazenada nas seguintes variáveis: 
matéria1, matéria2 e matéria3.'''

def aprovado(matéria1, matéria2, matéria3):
  if matéria1>7 and matéria2>7 and matéria3>7:
    return True
print(aprovado(8,9,8))
  
