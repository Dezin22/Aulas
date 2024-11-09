# https://dontpad.com/216-26-08


# 																			ASSOCIAÇÃO
# ============================================================================================================================================================


# DEF __INIT__(SELF): --> METODO CONSTRUTOR DO NOSSO OBJETO
	
# 																		ASSOCIAÇÃO UNILATERAL 

class Autor:#classe Autor
    def __init__(self,nome:str,idade:int) -> None:
        self.nome = nome 
        self.idade = idade 

class Livro:
    def __init__(self,titulo:str,ano_publi:int,autor:Autor) -> None:
        self.titulo = titulo 
        self.ano_publi = ano_publi
        self.autor = autor
        self.autor_nome = autor.nome 
        self.autor_idade = autor.idade 
# a1 = Autor("CS Lewis",100)
# l1 = Livro("O sobrinho do mago",2003,a1)

# print(l1.autor_nome)


# =============================================================================================================================================
# 																			ASSOCIAÇÃO BILATERAL



class Livro:
    def __init__(self,titulo:str,autor:str) -> None:
        self.titulo = titulo 
        self.autor = autor 
        self.disponivel = True 

l1 = Livro("O sobrinho do mago","CS Lewis")

class Biblioteca:
    def __init__(self) -> None:
        self.catalogo = [ ]#inicia uma lista vazia de livros

    def adicionar_livro(self,livro:Livro):
        self.catalogo.append(livro)

    def emprestar_livro(self,livro:Livro):#metodo que administra a classe livro mudando o status de disponivel True para False 
        livro.disponivel = False 

b1 = Biblioteca()
print(b1.catalogo)
b1.adicionar_livro(vars(l1))
print(b1.catalogo)
b1.emprestar_livro(l1)
print(b1.catalogo)

# ==========================================================================================================================================================

# ENCAPSULAMENTO

# dois underlines "__" tem a função de privar nossa classe deixando assim o código mais bem estruturado 
								
class Pessoa:
    def __init__(self,nome,telefone,cpf) -> None:
        self.__nome = nome
        self.__telefone = telefone
        self.__cpf = cpf

    def get_nome(self):
        return self.__nome
    
    def set_nome(self,novo_nome)->None:
        self.__nome = novo_nome


p1 = Pessoa("Gabriel","31971319392","12345678911")
print(p1.get_nome())#
p1.set_nome("Felipão")
print(p1.get_nome())#
#print(p1.__telefone)#
#print(p1.__cpf)#