class Produto:
    def __init__(self, nome, preco, quantidade, codigo_produto, categoria):
        self.nome = nome
        self.preco =  preco
        self.quantidade = quantidade
        self.codigo_produto = codigo_produto
        self.categoria = categoria

    
    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_preco(self):
        return self.preco

    def set_preco(self, preco):
        self.preco = preco

    def get_quantidade(self):
        return self.quantidade

    def set_quantidade(self, quantidade):
        self.quantidade = quantidade

    def get_codigo_produto(self):
        return self.codigo_produto

    def set_codigo_produto(self, codigo_produto):
        self.codigo_produto = codigo_produto

    def get_categoria(self):
        return self.categoria

    def set_categoria(self, categoria):
        self.categoria = categoria

class SistemaCadastro:
    def __init__(self):
        self.produtos = []

    def criarProduto(self, nome, preco, quantidade, codigo_produto, categoria):
        produto = Produto(nome, preco, quantidade, codigo_produto, categoria)
        self.produtos.append(produto)
        print("Produto cadastrado com sucesso!")

    def listarProdutos(self):
        if len(self.produtos) == 0:
            print("Não há produtos cadastrados.")
        else:
            for produto in self.produtos:
                print("-------------------------")
                print(f"Nome: {produto.get_nome()}")
                print(f"Preço: {produto.get_preco()}")
                print(f"Quantidade: {produto.get_quantidade()}")
                print(f"Código do Produto: {produto.get_codigo_produto()}")
                print(f"Categoria: {produto.get_categoria()}")

    def atualizarProduto(self):
        if len(self.produtos) == 0:
            print("Não há produtos cadastrados.")
        else:
            codigo = int(input("Digite o código do produto que deseja atualizar: "))

            for produto in self.produtos:
                if produto.get_codigo_produto() == codigo:
                    print("-------------------------")
                    print(f"Nome: {produto.get_nome()}")
                    print(f"Preço: {produto.get_preco()}")
                    print(f"Quantidade: {produto.get_quantidade()}")
                    print(f"Código do Produto: {produto.get_codigo_produto()}")
                    print(f"Categoria: {produto.get_categoria()}")
                    print("-------------------------")
                    op = int(input("O que deseja atualizar?\n 1 - Nome\n 2 - Preço\n 3 - Quantidade\n 4 - Categoria\n-------------------------\n"))

                    match op:
                        case 1:
                            nome = input("Digite o novo nome: ")
                            produto.set_nome(nome)
                        case 2:
                            preco = float(input("Digite o novo preço: "))
                            produto.set_preco(preco)
                        case 3:
                            quantidade = int(input("Digite a nova quantidade: "))
                            produto.set_quantidade(quantidade)
                        case 4:
                            categoria = input("Digite a nova categoria: ")
                            produto.set_categoria(categoria)
                        case _:
                            print("Opção inválida!")
                else:
                    print("Produto não encontrado.")

    def deletarProduto(self):
        if len(self.produtos) == 0:
            print("Não há produtos cadastrados.")
        else:
            print("-------------------------")
            codigo = int(input("Digite o código do produto que deseja deletar: "))

            for produto in self.produtos:
                if produto.get_codigo_produto() == codigo:
                    self.produtos.remove(produto)
                    print("Produto deletado com sucesso!")
                else:
                    print("Produto não encontrado.")
