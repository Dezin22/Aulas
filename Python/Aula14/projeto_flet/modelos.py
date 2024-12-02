import random
import string
from datetime import datetime

class Cliente:
    def __init__(self,nome:str,cpf:int,email:str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.email = email

class Quarto:
    def __init__(self,numero:int,disponibilidade:True,camas:int) -> None:
        self.numero = numero
        self.disponibilidade = disponibilidade
        self.camas = camas

   
class Reserva:
    def __init__(self,cliente:Cliente) -> None:
        self.nome = cliente.nome
        self.cpf = cliente.cpf
        self.email = cliente.email
        self.data = datetime.now().strftime("%d/%m/%Y")
    
        def gerar_numero_reserva():
        # Parte da data e hora
            data_hora = datetime.now().strftime("%Y%m%d%H%M%S")
        # Parte aleatória com letras e números
            caracteres_aleatorios = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        # Número de reserva final
            numero_reserva = f"RES{data_hora}{caracteres_aleatorios}"
            return numero_reserva    
        self.reserva = gerar_numero_reserva()
class Gerenciador_de_Reserva:
    def __init__(self) -> None:
        self.lista_reserva = []
    
    def adicionar_reserva(self,reserva:Reserva):
        self.lista_reserva.append(reserva)
        
        
        
c1 = Cliente('Andre',10000000,'sdadasda@awsdasdas')
r1 = Reserva(c1)
g1 = Gerenciador_de_Reserva()
print(vars(g1))
g1.adicionar_reserva(vars(r1))
c2 = Cliente('rteste',1216124151,'teste@teste')
r2 = Reserva(c2)
g1.adicionar_reserva(vars(r2))
print(vars(g1))