from db import conectar

def adicionar_produto(nome, quantidade, preco):
    con = conectar()
    cur = con.cursor()
    cur.execute("INSERT INTO produtos (nome, quantidade, preco) VALUES (?, ?, ?)",
                (nome, quantidade, preco))
    con.commit()
    con.close()

def listar_produtos():
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT id, nome, quantidade, preco FROM produtos")
    produtos = cur.fetchall()
    con.close()
    return produtos

def atualizar_estoque(produto_id, quantidade, tipo):
    con = conectar()
    cur = con.cursor()

    if tipo == 'entrada':
        cur.execute("UPDATE produtos SET quantidade = quantidade + ? WHERE id = ?", (quantidade, produto_id))
    elif tipo == 'saida':
        cur.execute("UPDATE produtos SET quantidade = quantidade - ? WHERE id = ?", (quantidade, produto_id))

    cur.execute("INSERT INTO movimentacoes (produto_id, tipo, quantidade) VALUES (?, ?, ?)",
                (produto_id, tipo, quantidade))
    con.commit()
    con.close()

def produtos_com_estoque_baixo(limite=5):
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT id, nome, quantidade FROM produtos WHERE quantidade <= ?", (limite,))
    produtos = cur.fetchall()
    con.close()
    return produtos
