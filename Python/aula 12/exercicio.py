class Animal:
     def __init__(self,nome,idade,cor_pelo) -> None:
          self.nome = nome
          self.idade = idade 
          self.cor_pelo = cor_pelo


class Cachorro(Animal):
    def __init__(self, nome, idade, raca,cor_pelo,) -> None:
         super().__init__(nome, idade, cor_pelo)
         self.raca = raca
    
    def latir(self):
         return "Wooofs"


class Gato(Animal):
    def __init__(self, nome, idade, cor_pelo) -> None:
         super().__init__(nome, idade, cor_pelo)#super fica responsavel por pegar as caracteristicas de Animal
    

    def miar(self):
         return "miau"


cachorro = Cachorro("Gergelin",1,"vira lata","caramelo")
gato = Gato("Xanin","10","alaranjado")
