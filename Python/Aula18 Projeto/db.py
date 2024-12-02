import mysql.connector as mysql

class Produto:
    def __init__(self, nome: str, desc: str, quant: int, pu: float, cb: str) -> None:
        self.id = None
        self.nome = nome
        self.desc = desc
        self.quant = quant
        self.pu = pu
        self.cb = cb

class Estoque:
    def __init__(self) -> None:
        self.connection = None
        self.cursor = None

    def db(self):
        try:
            self.connection = mysql.connect(
                host='localhost',
                port=3306,
                user='root',
                password='In@12345678',
                database='projeto'
            )
        except mysql.Error as e:
            print(f"\033[31mErro ao conectar ao banco de dados: {e}\033[m")
            return False

        print("\033[32mConexão com o banco estabelecida com sucesso!\033[m")
        return True

    def cadastrar_produto(self, prod: Produto):
       
        self.cursor = self.connection.cursor()
        inserir = 'INSERT INTO estoque (nome, descricao, quantidade, preco_unitario, codigo_de_barras) VALUES (%s, %s, %s, %s, %s);'
        self.cursor.execute(inserir, (prod.nome, prod.desc, prod.quant, prod.pu, prod.cb))
        self.connection.commit()
        self.cursor.close()
        

    def lista_estoque(self):
    
        self.cursor = self.connection.cursor()
        self.cursor.execute('SELECT * FROM estoque;')
        res = self.cursor.fetchall()
        self.cursor.close()
        return res

    def deletar_produto(self, id_produto):
    
        self.cursor = self.connection.cursor()
        deletar = 'DELETE FROM estoque WHERE id = %s;'
        self.cursor.execute(deletar, (id_produto,))
        self.connection.commit()
        self.cursor.close()
    
    def atualizar_produto(self, id_produto, nome: str, desc: str, quant: int, pu: float, cb: str):
 
        self.cursor = self.connection.cursor()
        sql_update_query = '''UPDATE estoque 
                              SET nome = %s, descricao = %s, quantidade = %s, preco_unitario = %s, codigo_barras = %s 
                              WHERE id = %s;'''
        self.cursor.execute(sql_update_query, (nome, desc, quant, pu, cb, id_produto))
        self.connection.commit()
        self.cursor.close()

    def retirar_produto(self, id_produto, quantidade: int):

        self.cursor = self.connection.cursor()
        # Primeiro, vamos verificar a quantidade atual
        self.cursor.execute('SELECT quantidade FROM estoque WHERE id = %s;', (id_produto,))
        resultado = self.cursor.fetchone()
        
        if resultado:
            quantidade_atual = resultado[0]
            if quantidade_atual >= quantidade:
                nova_quantidade = quantidade_atual - quantidade
                sql_update_query = 'UPDATE estoque SET quantidade = %s WHERE id = %s;'
                self.cursor.execute(sql_update_query, (nova_quantidade, id_produto))
                self.connection.commit()
                print(f"{quantidade} unidades do produto ID {id_produto} foram vendidas!")
            else:
                print(f"\033[31mNão há quantidade suficiente para vender. Disponível: {quantidade_atual}\033[m")
        else:
            print("\033[31mProduto não encontrado!\033[m")

        self.cursor.close()

class Venda:
    def __init__(self, estoque: Estoque) -> None:
        self.estoque = estoque

    def realizar_venda(self, id_produto: int, quantidade: int):
        self.estoque.retirar_produto(id_produto, quantidade)
