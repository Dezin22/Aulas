# https://dontpad.com/216-02-09
# https://numba.readthedocs.io/en/stable/user/performance-tips.html

#Criar um entidade estoque 
#CRUD
#CREATE CRIAR 
#READ  LER
#UPDATE  ATUALIZAR
#DELETE  DELETAR


# ===========================================================================
# main.py


from dataclasses import dataclass

class Produto:
    def __init__(self,nome:str, preco:float) -> None:#metodo construtor
        self.nome = nome
        self.quantidade = 0
        self.preco =float(f"{preco:2f}") 


@dataclass 

class Estoque:
    def __init__(self) -> None:# MEtodo construtor 
        self.lista_produto = [] #Inicia com valor padrão vazio

    def cadastrar_produto(self,produto:Produto):
        """
        produto -> recebe um objeto da classe Produto 
        Cadastrar meu objeto na lista de produtos -> lista_produto
        """
        self.lista_produto.append(vars(produto))#

    def adicionar_item_ao_estoque(self,produto):
        for produto in self.lista_produto:
            for chave,valor in produto.items():
            







nome_produto = str(input("Digite o nome do produto"))
quantidade_produto = input("Digite o quantidade do produto")
preco_produto = float(input("Digite o preco do produto"))
preco_produto = preco_produto


p1 = Produto(nome_produto,preco_produto)
e1 = Estoque()

print(e1.lista_produto)
e1.cadastrar_produto(p1)
print(e1.lista_produto)
e1.adicionar_item_ao_estoque(p1)





# ============================================================================================================================
class Produto:
    def __init__(self,nome ,preco) -> None:
        self.nome = nome 
        self.quantidade = 0
        self.preco = preco 

class Estoque:
    def __init__(self) -> None:
        self.estoque_produtos = []

    def adicionar_produto(self,produto:Produto):
        self.estoque_produtos.append(vars(produto))
        
    def adicionar_item_ao_estoque(self,quantidade_a_ser_adicionado):
        nome_do_produto = input("Digite o nome do produto")

        for produto in self.estoque_produtos:
            for chave in produto:
                print(chave)

p1 = Produto(nome="salame",preco=12.50)
e1 = Estoque()# Objeto da classse estoque
print(e1.estoque_produtos)# estoque de produtos
e1.adicionar_produto(p1)# adicinando produtos ao estoque
print(e1.estoque_produtos)
e1.adicionar_item_ao_estoque(15)
print(e1.estoque_produtos)







