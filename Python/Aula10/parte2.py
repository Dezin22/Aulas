import flet as ft
from time import sleep
def main(pagina:ft.Page):#
    usuarios = []

    def cadastrar(e):
        nome = nome_input.value
        senha = senha_input.value
        pagina.controls.append(ft.Text("Usuario cadastrado com sucesso"))
        

        pagina.update()

      

        usuarios.append([nome,senha])




    def listar_usuarios(e):
        print(usuarios)
        pagina.controls.append(ft.Text(f'{usuarios}'))
        pagina.update()

    pagina.bgcolor = "dark"
    titulo = ft.Text("Menu de cadastro",size=50,color=ft.colors.BLUE)
    nome_input = ft.TextField(hint_text="Digite seu nome")
    senha_input = ft.TextField(hint_text="Digite sua senha",password=True)
    cadastrar_usuario= ft.ElevatedButton(text="Cadastrar",on_click=cadastrar)
    listar_usuario = ft.ElevatedButton(text="Listar",on_click=listar_usuarios)

    pagina.add(titulo,nome_input,senha_input,cadastrar_usuario,listar_usuario)
    
    pagina.update()
    
ft.app(target=main)