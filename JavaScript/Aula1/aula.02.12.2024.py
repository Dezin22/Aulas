# Funções

# Ao definir uma função utilizamos a palavra reservada def com a seguinte sintaxe:

# def minha_função (parâmetro 1, parâmetro 2...):
# ... corpo da função
# return resultado

# Entrada: Parâmetros
# Processamento: Corpo da Função
# Saída: Resultado

def somar (n1, n2):
    return n1 + n2

# Utilizar a função
numero1 = int(input('Digite um número: '))
numero1 = int(input('Digite outro número: '))


def mostrar_info(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')

mostrar_info(nome='João', idade=30, cidade='exemplo')


def mostrar_info ()