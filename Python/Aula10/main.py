import flet as ft

def main(page:ft.Page):
    page.bgcolor = ft.colors.RED_400
    titulo = ft.Text(value='Cadastro', size=30, color='Black')
    page.title = 'Cadastro'
    page.add(
        ft.AppBar(title=ft.Text('Cadastro de Cartão'),
                  center_title=True
                  
                  ),
        ft.FilledButton(text='Globo Esporte', url='https://ge.globo.com/?utm_source=globo.com&utm_medium=header'),
        ft.FilledButton(text='Instagram', url='https://instagram.com'),
        ft.TextField(hint_text='Digite o CPF', color='Black', input_filter=ft.InputFilter(allow=True, regex_string=r'[0-9]', replacement_string='')),
        ft.TextField(hint_text='Digite o numero do Cartão', color='Black', input_filter=ft.InputFilter(allow=True, regex_string=r'[0-9]', replacement_string='')),
        ft.TextField(label="Digite a senha", password=True, can_reveal_password=True),
        ft.FilledButton('Cadastrar', icon='add', icon_color='Red'),)
    page.update()

ft.app(target=main)