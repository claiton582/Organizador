import sqlite3

connection = sqlite3.connect('organizador.db')

c = connection.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS organizador(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(90) NOT NULL,
        genero STR(90) NOT NULL,
        horas INTEGER,
        data INTEGER
)
    
""")