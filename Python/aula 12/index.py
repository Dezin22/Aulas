# 2 - Formas Geométricas https://dontpad.com/216-19-08

# Crie uma classe base Forma com um método calcular_area().
# Crie duas subclasses Circulo e Retangulo que implementam o método calcular_area() de acordo 
# com suas fórmulas específicas. Adicione um atributo adicional em Circulo para o raio e em Retangulo 
# para a largura e altura.

class Forma:
    def __init__(self,nome) -> None:
        self.nome = nome
    def calcular(self):
        pass
class quadrado(Forma):
    def calcular(self):
        cal = int(input('Digite a valor de um dos lados do quadrado: '))
        if cal > 0:
            print(cal**2)
        else:
            print('Valor incorreto!')
        return ''
class triangulo(Forma):
    def calcular(self):
        base = int(input('Digite a valor da base do triangulo: '))
        altura = int(input('Digite a altura do triangulo: '))
        resultado = base * altura /2
        print(resultado)

quadrado = quadrado('quadrado')
triangulo = triangulo('triangulo')

print(quadrado.nome, quadrado.calcular())