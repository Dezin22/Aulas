# 1 - Funcionários e Tipos de Funcionário
# Crie uma classe base Funcionario com atributos nome e salario. 
# Crie subclasses Gerente e Desenvolvedor que adicionam atributos adicionais 
# (departamento para Gerente e linguagem_programacao para Desenvolvedor). 
# Implemente um método aumentar_salario() que aplica um aumento no salário com base no tipo de funcionário
from typing import Any


class Funcionario:
    def __init__(self,nome,salario) -> None:
        self.nome = nome
        self.salario = salario
    
    def aumentar_salario(self,acrescimo):
        self.salario += acrescimo
        
    
class Gerente(Funcionario):
    def __init__(self, nome, salario,departamento) -> None:
        super().__init__(nome, salario)
        self.departamento = departamento

class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario,linguagem_programacao) -> None:
        super().__init__(nome, salario)
        self.linguagem_programacao = linguagem_programacao
        
g1 = Gerente('Carlos',8000,'Camara de frios')
d1 = Desenvolvedor('Andre',3000,'python')

print(vars(g1))
g1.aumentar_salario(300)
print(vars(g1))

print(vars(d1))
d1.aumentar_salario()
print(vars(d1))
