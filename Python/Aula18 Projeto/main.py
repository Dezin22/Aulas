from db import Produto,Estoque,Venda
import flet as ft

def main(page: ft.page):
    def cadastrar(e):
        e1 = Estoque(p1)
        p1 = Produto({tb1.value},{tb2.value},{tb3.value},{tb4.value},{tb5.value})
        e1.cadastrar_produto()
        page.update()
        


    tb1 = ft.TextField(label='Nome do Produto')
    tb2 = ft.TextField(label='Descrição')
    tb3 = ft.TextField(label='Quantidade')
    tb4 = ft.TextField(label='Preço Unitário')
    tb5 = ft.TextField(label='Codigo de Barra')
    b = ft.ElevatedButton(text="Cadastrar", on_click=cadastrar)
    page.add(tb1,tb2,tb3,tb4,tb5,b)

    
ft.app(main)

