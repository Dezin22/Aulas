# Crie uma classe Automovel (pai) que contenha caracteristicas como modelo,ano,cor 
#atributo velocidade que começa em zero
# adicione 2 metodos : acelerar e frear 
# crie duas subclasses Carro e Bike

class Automovel:
    def __init__(self,modelo,ano,cor) -> None:
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0

class Carro(Automovel):
    def __init__(self, modelo, ano, cor) -> None:
        super().__init__(modelo, ano, cor)

    
    def acelerar(self):
        self.velocidade += 10
        pass
    
    def frear(self):
        if self.velocidade >= 5:
            self.velocidade -= 5
        else:
            print('O carro está parado ou parando.')

class Bicicleta(Automovel):
    def __init__(self, modelo, ano, cor) -> None:
        super().__init__(modelo, ano, cor)
    
    def acelerar(self):
        self.velocidade += 2
        pass
    
    def frear(self):
        if self.velocidade >1:
            self.velocidade -= 1
        else:
            print('A bike já está parada')

c1 = Carro('Fiat',2010,'preto')
b1 = Bicicleta('Monark',1998,'Branca')

print(vars(c1))
