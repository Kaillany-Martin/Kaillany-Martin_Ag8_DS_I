#entrada boas vindas
print("Pesquisa de Opinião \n Grau de satisfação no atendimento ao cliente.\n")

#contadores
excelente = 0
ruim = 0

#entrada de dados repetidos
for i in range(50):

    nome = input("Nome:")
    idade = int(input("Idade:"))
    satisfacao = int(input("Qual seu nível de satisfação com o atendimento prestado?\n 1- Excelente \n 2- Bom \n 3- Ruim \n Sua resposta:"))
#estrutura de decisão
    if satisfacao == 1:
         excelente += 1
    elif satisfacao == 3:
         ruim += 1

#saída
print("\n Resultado da pesquisa de satisfação:")
print(f"Quantidade de respostas 'Excelente': \n {excelente}")
print(f"Quantidade de respostas 'Ruim': \n {ruim}")