# Desenvolva um aplicativo de gerenciamento de tarefas
# em python. Crie duas classes, Tarefa e Projeto, com uma
# associação unidirecional. Permita que as tarefas sejam
# associadas a projetos e que você possa listar as tarefas
# de um projeto em particular.


print('Bem vindo ao menu do Projeto')

class Tarefa:
    def __init__(self,descricao:str,tipo:str) -> None:
        self.descricao = descricao
        self.tipo = tipo
    
        
t1 = Tarefa(str(input('Digite a descrição da tarefa: ')),str(input('Digite o tipo da tarefa: ')))
class Projeto:
    def __init__(self,nome:str,tarefa:Tarefa) -> None:
        self.nome = nome
        self.descricao = tarefa.descricao
        self.tipo = tarefa.tipo

p1 = Projeto(str(input('Digite o nome do seu projeto: ')),t1)
print(vars(p1))