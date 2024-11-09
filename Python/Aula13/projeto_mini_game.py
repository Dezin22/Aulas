
from random import randint# gera um numero aleatorio em um intervalo determinado 

#Fazer uma classe Personagem que tenha como atributos : nome,nivel,vida,xp
#e tenha como metodos --> gerar_dano() 
class Personagem:
    def __init__(self,nome) -> None:
        self.nome = nome 
        self.nivel = 1# inicia meu personagem no nivel 1 JUninho
        self.vida = 100 # barra de vida cheia 
        self.xp = 0

   
# Criar 2 objetos da classe Personagem
p1 = Personagem("Liu keng")
p2 = Personagem("JOOHNY CAGE")

# Criar a classe Player/Jogador  que contenha como caracteristicas nome do jogador, personagem
# MEtodo gerar dano --> 
#Criar 2 objeto da classe 2

class Jogador:
    def __init__(self,nome:str,personagem:Personagem) -> None:
        self.nome = nome
        self.personagem = personagem

    def gerar_dano(self,personagem:Personagem,adversario:Personagem):
        print("\033[31mGerando dano\0332[m")
        match personagem.nivel:
            case 1:
                adversario.vida -= 10
            case 2:
                adversario.vida -= 12
            case 3:
                adversario.vida -= 13
            case 4:
                adversario.vida -= 14
            case 4:
                adversario.vida -= 15
            case 5:
                adversario.vida -= 16
            case 1:
                adversario.vida -= 17
                


        personagem.xp += 10
        if personagem.xp >=100:
            personagem.xp =0
            personagem.nivel +=1
            print("\033[32mParabens voce subiu de nivel \033[m")


j1 = Jogador("Paulin o Loko",p1)
j2 = Jogador("Jalinho",p2)


while True:
    perg = input("Voce deseja gerar dano ?").lower()
    if perg =="sim":
        j1.gerar_dano(p1,p2)
        print(j2.personagem.vida)
    else:
        break