class Veiculo:
    def __init__(self,cor,placa,velocidade,documento,rodas) -> None:
        self.cor = cor 
        self.placa = placa
        self.velocidade = velocidade
        self.documento = documento
        self.rodas = rodas
class Carro(Veiculo):
    def __init__(self,cor,placa,velocidade,documento,rodas,portas) -> None:
        super().__init__(cor, placa, velocidade, documento, rodas)
        self.portas = portas
    def mover(self):
        return 'O carro está se movendo'

class Moto(Veiculo):
    def __init__(self, cor, placa, velocidade, documento, rodas) -> None:
        super().__init__(cor, placa, velocidade, documento, rodas)
        
    def mover(self):
        return 'a moto está se movendo'
c1 = Carro('Vermelho','hhh-1234',80,'asdhasgdajsdbajk',4,5)
m1 = Moto('Preta','hhh-1234',60,'asdfgisgnsdgm',2)

print(vars(c1))
print(vars(m1))    
        