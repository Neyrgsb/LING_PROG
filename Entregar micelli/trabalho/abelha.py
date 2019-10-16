# -*- coding: utf-8 -*-

import teste1,random
import sqlite3
'''
numcal30 = int(teste1.cal30)
numcal40 = int(teste1.cal40)
nummuz30 = int(teste1.muz30)
nummuz40 = int(teste1.muz40)
numfcp30 = int(teste1.fcp30)
numfcp40 = int(teste1.fcp40)
nummar30 = int(teste1.mar30)
nummar40 = int(teste1.mar40)
'''

class Pizzas:
    def __init__(self,nome,tamanho,preco):
       self.nome = nome
       self.tamanho = tamanho
       self.preco = preco

cal30 = Pizzas("CALABRESA", 30, 35.9)

cal40 = Pizzas("CALABRESA", 40, 59.9)

muz30 = Pizzas("MUZZARELA", 30, 32.9)

muz40 = Pizzas("MUZZARELA", 40, 53.9)

fcp30 = Pizzas("FRANGO COM CATUPITY", 30, 39.9)

fcp40 = Pizzas("FRANGO COM CATUPITY", 40, 63.9)

mar30 = Pizzas("MARGHERITTA", 30, 33.9)

mar40 = Pizzas("MARGHERITTA", 40, 54.9)

def Calcular(a,b,c,d,e,f,g,h):

    preco = a*cal30.preco+b*cal40.preco+c*muz30.preco+d*muz40.preco+ e*fcp30.preco+f*fcp40.preco+g*mar30.preco+h*mar40.preco
    print(preco)
    return preco

def codigo():
    for x in range(10):
        code = random.randint(100000,999999)
    return code


def cancelar():
    conn = sqlite3.connect('pedido.db')
    cursor = conn.cursor()

    codigo = int(input("Escreva o seu codigo para cancelar"))
    cursor.execute("""
    DELETE FROM carrinho
    WHERE codigo = ?
    """, (codigo,))

    conn.commit()
