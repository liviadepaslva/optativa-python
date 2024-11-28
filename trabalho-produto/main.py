from classes import Produto
from classes import SistemaCadastro

sistema = SistemaCadastro()

print("Bem-vindo ao sistema de produtos!")
while True:
    print("-------------------------")
    op = int(input("Selecione a operação desejada:\n 1 - Cadastrar Produto\n 2 - Listar Produtos\n 3 - Atualizar Produto\n 4 - Deletar Produto\n Digite outro número para sair.\n-------------------------\n"))

    match op:
        case 1:
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            quantidade = int(input("Digite a quantidade do produto: "))
            codigo_produto = int(input("Digite o código do produto: "))
            categoria = input("Digite a categoria do produto: ")

            sistema.criarProduto(nome, preco, quantidade, codigo_produto, categoria)
        case 2:
            sistema.listarProdutos()
        case 3:
            sistema.atualizarProduto()
        case 4:
            sistema.deletarProduto()
        case _:
            print("Saindo...")
            break