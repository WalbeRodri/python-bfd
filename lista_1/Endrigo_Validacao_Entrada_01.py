# Aluno: Thiago Endrigo
# Prof.: Walber Olibeira
# Turma: 11.

# Validação de Entrada:
# Crie um programa que peça ao usuário para inserir uma nota entre 0 e 10. 
# O programa deve continuar pedindo a entrada até que o usuário insira um valor inválido...

notas = []
nota = 0
while nota <= 0 or nota <= 10:
    nota = int(input("Informe as notas de 0 a 10: "))
    notas.append(nota)
    if nota > 10:
        notas.pop()
    
print("Voce informou um valor inválido, programa será encerrado.")
print('Segue a lista das notas informadas: ', notas)
    
    
