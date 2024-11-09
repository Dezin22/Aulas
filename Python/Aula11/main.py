class Pessoa:
    def __init__(self,nome,idade,cpf) -> None:# metodo construtor
        #atributos ou caracteristicas da minha função
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        
    def trabalhar(self):
        return('Estou trabalhando')
        
class Cachorro:
    def __init__(self,nome,raca,cor,idade) -> None:
        self.nome = nome
        self.raca = raca 
        self.cor = cor 
        self.idade = idade 

    def __repr__(self) -> str:# representa meu objeto 
        return f"O nome do cachorro é {self.nome} a idade é {self.idade} a cor é {self.cor} e a raça é {self.raca}"

    def latir(self):
        return "Ruuufs" 


c1 = Cachorro("geraldo felipe","Vira lata","preto",10)



luiz_guilherme = Pessoa("Luiz",22,"02145678911")
print(luiz_guilherme.idade)
print(luiz_guilherme.trabalhar())

luiz_guilherme.trabalhar()

print(c1)
print(c1.nome)
print(c1.raca)
print(c1.idade)
print(c1.cor)
print(c1.latir())
c1.latir()
print(vars(c1))


