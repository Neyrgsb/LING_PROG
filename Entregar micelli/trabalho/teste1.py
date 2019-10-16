from flask import Flask, request, render_template
import sqlite3, abelha, random

app = Flask(__name__)

cal30=0
cal40=0
muz30=0
muz40=0
fcp30=0
fcp40=0
mar30=0
mar40=0
code=0
precototal=0

@app.route('/')
def index():
     return render_template('pagina inicial1.html')

@app.route('/pedido', methods=['POST', 'GET'])
def pedido():

        return render_template('teste13.html')

@app.route('/echo2', methods=['POST', 'GET'])
def echo2():

    code = abelha.codigo()

    cal30 = str(request.form['p130'])
    if cal30=='':
        cal30='0'
    cal40 = str(request.form['p140'])
    if cal40=='':
        cal40='0'
    muz30 = str(request.form['p230'])
    if muz30=='':
        muz30='0'
    muz40 = str(request.form['p240'])
    if muz40=='':
        muz40='0'
    fcp30 = str(request.form['p330'])
    if fcp30=='':
        fcp30='0'
    fcp40 = str(request.form['p340'])
    if fcp40=='':
        fcp40='0'
    mar30 = str(request.form['p430'])
    if mar30=='':
        mar30='0'
    mar40 = str(request.form['p440'])
    if mar40=='':
        mar40='0'
    conn = sqlite3.connect('pedido.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS carrinho (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            
            codigo INTEGER,
            cal30 TEXT,
            cal40 TEXT,
            muz30 TEXT,
            muz40 TEXT,
            fcp30 TEXT,
            fcp40 TEXT,
            mar30 TEXT,
            mar40 TEXT,
            nome TEXT,
            ende TEXT,
            tel TEXT,
            pag TEXT
    );
    """)
    cursor.execute("""
    INSERT INTO carrinho (codigo,cal30,cal40,muz30,muz40,fcp30,fcp40,mar30,mar40)
    VALUES (?,?,?,?,?,?,?,?,?)
    """, (code,cal30,cal40,muz30,muz40,fcp30,fcp40,mar30,mar40))
    conn.commit()

    cursor.execute("""
    SELECT * FROM carrinho;
    """)

    for linha in cursor.fetchall():
        print(linha)

    conn.close()

    precototal = abelha.Calcular(int(cal30),int(cal40),int(muz30),int(muz40),int(fcp30),int(fcp40),int(mar30),int(mar40))

    return render_template('dados.html', preco=precototal, code=code)


@app.route('/sucesso', methods=['POST', 'GET'])
def sucesso():


    nome = request.form['nome'].upper()
    endereco = request.form['ende']
    tel = request.form['telefone']
    pag = request.form['forma']


    conn = sqlite3.connect('pedido.db')
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE carrinho
    SET nome = ?, ende = ?, tel = ?, pag = ?
    WHERE id = (SELECT MAX(id) FROM carrinho);
    """, (nome, endereco, tel, pag))
    conn.commit()


    cursor.execute("""
        SELECT * FROM carrinho;
        """)

    for linha in cursor.fetchall():
        print(linha)

    #abelha.cancelar()

    cursor.execute("""
        SELECT * FROM carrinho;
        """)

    for linha in cursor.fetchall():
        print(linha)

    conn.close()


    return render_template('sucesso.html')


@app.route('/home', methods=['GET'])
def echohome():
    return render_template('pagina inicial1.html')    

@app.route('/vinho', methods=['GET'])
def vinho():
    return render_template('vinhos.html')

@app.route('/contato', methods=['GET'])
def contato():
    return render_template('contato.html')

@app.route('/cardapio', methods=['GET'])
def cardapio():
    return render_template('cardapio.html')

@app.route('/carrinho', methods=['GET'])
def carrinho():
    return render_template('construçao.html')





if __name__ == "__main__":
    app.run()