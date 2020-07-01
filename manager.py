import sqlite3

class Connect(object):
    def __init__(self,db_name):
        try:
            self.connection = sqlite3.connect(db_name)
            self.c = self.connection.cursor()
        except sqlite3.Error:
            print("Erro ao abrir o banco.")

    def commit_db(self):
        if self.c:
            self.connection.commit()

    def close_db(self):
        if self.c:
            self.connection.close()
            print("conexão fechada.")


class Organizador(object):
    tb_name = 'organizador'

    def __init__(self):
        self.db = Connect('organizador.db')
        self.tb_name


    def cadastra_game(self):
        self.nome = input("Nome do jogo: ")
        self.genero = input("Genero do jogo: ")
        self.horas = input("horas para terminar o jogo: ")
        self.data = input("Data de lançamento: ")
        try:
            self.db.c.execute("""
            INSERT INTO organizador(nome,genero,horas,data)
            VALUES(?,?,?,?)
            """,(self.nome,self.genero,self.horas,self.data))
            self.db.commit_db()

        except sqlite3.IntegrityError:
            return False

    def ler_games(self):
        sql = 'SELECT id,nome,genero,horas,data FROM organizador ORDER BY nome'
        r = self.db.c.execute(sql)
        return r.fetchall()


    def imprimir_games(self):
        lstGames = self.ler_games()
        print('{:>3s} {:5} {:3s} {:3s} {:3s} ' .format(
            'id', 'nome','genero', 'horas', 'lancado',))

        for d in lstGames:
            print(d)


    def localizar_genero(self):
        while True:
            self.genero = input("Digite o genero do jogo: ")


            if self.genero:
                r = self.db.c.execute('SELECT * FROM organizador WHERE genero =?',(self.genero,))
                self.db.commit_db()
                return r.fetchall()

                
    def imprimir_genero(self):
        self.localizar_genero()
        lstDeGenero = self.localizar_genero()
        for d in lstDeGenero:
            print(d)


    def localizar_acima(self):
        sql  = 'SELECT * FROM organizador WHERE horas >=30 '
        r = self.db.c.execute(sql)
        return r.fetchall()

    def imprimir_acima(self):
        self.localizar_acima()
        lstAcima = self.localizar_acima()
        for a in lstAcima:
            print(a)

    def localizar_abaixo(self):
        sql = 'SELECT * FROM organizador WHERE horas <30'
        r = self.db.c.execute(sql)
        return r.fetchall()
    def imprimir_abaixo(self):
        self.localizar_abaixo()
        lstAbaixo = self.localizar_abaixo()
        for c in lstAbaixo:
            print(c)
O = Organizador()

#
#
#O.localizar_genero()
#O.imprimir_genero()
def menu():
    print("1- Cadastrar jogo \n2- Listar todos os jogos \n3- Buscar jogo por genero \n4- Buscar jogos com mais de 30 horas"
          " \n5- Buscar jogos com menos de 30 horas \n"
          "0- Sair")
    return int(input("Entre com a opção: "))
if __name__ == '__main__':
    O = Organizador()

    op = -1
    while op != 0:
        op = menu()
        if op==1:
            O.cadastra_game()
        elif op==2:
            O.imprimir_games()
        elif op==3:
            O.imprimir_genero()
        elif op == 4:
            O.imprimir_acima()
        elif op == 5:
           O.imprimir_abaixo()
