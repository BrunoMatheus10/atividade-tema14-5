# Função para calcular quantos dias de vida o usuário já viveu
# Considera que um ano tem 365 dias
def dias_de_vida(nome, idade):
    return idade * 365

# Leitura do nome e da idade do usuário
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

# Exibição do número aproximado de dias de vida
print(nome," você já viveu aproximadamente",dias_de_vida(nome, idade), "dias.")
