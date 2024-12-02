# Lista de exercicios 

# 								Nível Fácil

# 1. Criando um animal de estimação:

# Crie uma classe Animal com atributos como nome, idade e tipo.
# Implemente um método emitir_som() que retorne uma string genérica como "Fazendo algum som".
# Crie subclasses Cachorro, Gato e Passaro, sobrescrevendo o método emitir_som() para retornar sons específicos.
# Crie instâncias de cada classe e chame o método emitir_som().

# class Animal:
#     def __init__(self,nome) -> None:
#         self.nome = nome
#     def emitir_som(self):
#         pass
# class Cachorro:
#     def __init__(self,nome,idade,raca) -> None:
#         self.nome = nome
#         self.idade = idade
#         self.raca = raca
#     def emitir_som(self):
#         return 'Rouuff'
    
# a1 = Animal('Cachorro')
# c1 = Cachorro('Lobo', 5, 'Pastor')
# print(a1.nome)  
# print(vars(c1))  
# print(c1.emitir_som())
# 2. Criando um veículo:

# Crie uma classe Veiculo com atributos como marca, modelo e ano.
# Implemente um método mover() que retorne uma string genérica como "Movendo-se".
# Crie subclasses Carro, Moto e Bicicleta, sobrescrevendo o método mover() para retornar ações específicas.
# Crie instâncias de cada classe e chame o método mover().
# class Veiculo:
#     def __init__(self,marca,modelo,velocidade) -> None:
#         self.marca = marca
#         self.modelo = modelo
#         self.velocidade = velocidade
#     def mover(self):
#         if self.velocidade > 0:
#             print (f'O {self.marca} {self.modelo} está a {self.velocidade} Km/h')
#         else:
#             print (f'O veiculo está parado')      
#         return ''
# c1 = Veiculo(input('Escreva a marca do carro: '),input('Escreva o modelo do carro: '),int(input('Escreva a velocidade do carro: ')))


# print(c1.mover())
# 								Nível Médio

# 3. Criando formas geométricas:

# Crie uma classe Forma com atributos como cor e nome.
# Implemente um método calcular_area() que retorne uma mensagem indicando que a área não pode ser calculada para uma forma genérica.
# Crie subclasses Quadrado, Circulo e Triangulo, sobrescrevendo o método calcular_area() para calcular a área específica de cada forma.
# Crie instâncias de cada classe e chame o método calcular_area().
# class Forma:
#     def __init__(self,cor,nome,lado) -> None:
#         self.cor = cor
#         self.nome = nome
#         self.lado = lado
#     def calcular_area(self):
#         calculo = self.lado**2
#         print(f'O valor da area é {calculo} m²')
#         return''
# a1 = Forma('Branco', 'Quadrado', 4)
# print(a1.calcular_area())
        
# 4. Criando contas bancárias:

# Crie uma classe Conta com atributos como titular e saldo.
# Implemente métodos depositar() e sacar().
# Crie subclasses ContaCorrente e ContaPoupanca, adicionando funcionalidades específicas como taxa de manutenção ou rendimento.
# Crie instâncias de cada classe e realize operações bancárias.
class Conta:
    def __init__(self,titular,saldo) -> None:
        self.titular = titular
        self.saldo = saldo
    def depositar(self):
        print(f'Olá {self.titular} seu saldo atual é {self.saldo} reais')
        dep = int(input('Digite o valor do deposito: '))
        print(f'{self.titular} o seu novo saldo é {dep+self.saldo}')
        return''
    def sacar(self):
        print(f'Olá {self.titular} seu saldo atual é {self.saldo} reais')
        dep = int(input('Digite o valor do saque: '))
        print(f'{self.titular} o seu novo saldo é {dep-self.saldo}')
        return''
t1 = Conta('André', 500)
print(t1.depositar())
# 							Nível Difícil

# 5. Criando um jogo de RPG simples:

# Crie uma classe Personagem com atributos como nome, vida, ataque e defesa.
# Implemente métodos para atacar e defender.
# Crie subclasses Mago, Guerreiro e Ladrao, com habilidades e atributos específicos.
# Crie um sistema de combate entre personagens, utilizando a abstração para representar diferentes tipos de ataques e defesas.
class Personagem:
    def __init__(self,nome,vida,ataque,defesa) -> None:
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        class Mago:
            def __init__(self,magia,mana,estamina) -> None:
                  self.magia = magia
                  self.mana = mana
                  self.estamina = estamina
        class Guerreiro:
            def __init__(self,forca,mana,estamina) -> None:
                  self.forca = forca
                  self.mana = mana
                  self.estamina = estamina
        class Ladrao:
            def __init__(self,furtividade,mana,estamina) -> None:
                  self.furtividade = furtividade
                  self.mana = mana
                  self.estamina = estamina
# 6. Criando um sistema de e-commerce:

# Crie uma classe Produto com atributos como nome, preco e descricao.
# Crie uma classe Cliente com atributos como nome e endereco.
# Crie uma classe Pedido que relacione produtos e clientes.
# Implemente métodos para adicionar produtos ao carrinho, calcular o valor total do pedido e finalizar a compra.
