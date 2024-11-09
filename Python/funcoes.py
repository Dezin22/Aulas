

# Faça um sistema de uma padaria que 
# cadastre clientes contendo :
#  nome , email e telefone .dica(use um dicionario) em uma lista .

# ate que o dono da padaria digite no final do dia "parar" .

# logo em seguida sorteie um cliente para  receber um brinde (use a biblioteca random)
from random import choice



lista_de_cliente = []

def sorteio():
    num = choice(lista_de_cliente)
    print(num)
    
    
def menu():
    print("="*50)
    print("Menu Sistema".center(50))
    print("="*50)
    print('''
    1 - Cadastrar Cliente
    2 - Lista de Cliente
    3 - Sorteio
    4 - Parar
    ''')
    opcao = input('>>>-')
    return opcao

def cadastrar_cliente():
    dicionario = {}
    dicionario ['nome'] = str(input('digite o nome do cliente: '))
    dicionario ['email'] = str(input('digite o email do cliente '))
    dicionario ['telefone'] = str(input('o numero do cliente: '))
    lista_de_cliente.append(dicionario)

while True:
    retorno = menu()
    if retorno == '1':
        cadastrar_cliente()
    elif retorno == '2':
        print(lista_de_cliente)
    elif retorno == '3':
        sorteio()''
    elif retorno == '4':
        break
    else:
        print('opção invalida')