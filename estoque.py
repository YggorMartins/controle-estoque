from db import criar_tabelas
from models import *

def menu():
    print("\n--- Sistema de Controle de Estoque ---")
    print("1. Cadastrar novo produto")
    print("2. Entrada de estoque")
    print("3. Saída de estoque")
    print("4. Listar produtos")
    print("5. Produtos com estoque baixo")
    print("6. Sair")

def executar():
    criar_tabelas()

    while True:
        menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade inicial: "))
            preco = float(input("Preço unitário: "))
            adicionar_produto(nome, quantidade, preco)
            print("Produto adicionado com sucesso!")

        elif escolha == '2':
            id = int(input("ID do produto: "))
            quantidade = int(input("Quantidade para adicionar: "))
            atualizar_estoque(id, quantidade, 'entrada')
            print("Estoque atualizado com sucesso!")

        elif escolha == '3':
            id = int(input("ID do produto: "))
            quantidade = int(input("Quantidade para retirar: "))
            atualizar_estoque(id, quantidade, 'saida')
            print("Saída de estoque registrada!")

        elif escolha == '4':
            for p in listar_produtos():
                print(f"[{p[0]}] {p[1]} - Quantidade: {p[2]} - Preço: R${p[3]:.2f}")

        elif escolha == '5':
            baixos = produtos_com_estoque_baixo()
            print("Produtos com estoque baixo:")
            for p in baixos:
                print(f"[{p[0]}] {p[1]} - Quantidade: {p[2]}")
        
        elif escolha == '6':
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    executar()
