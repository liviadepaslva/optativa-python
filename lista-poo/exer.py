class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def resumo(self):
        return f'Nome: {self.nome}, Idade: {self.idade}'

class Pai(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.filhos = []

    def adicionar_filho(self, filho):
        self.filhos.append(filho)

    def resumo(self):
        filhos_nomes = ', '.join([filho.nome for filho in self.filhos])
        return f'Pai: {super().resumo()}, Filhos: {filhos_nomes}'

class Mae(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.filhos = []

    def adicionar_filho(self, filho):
        self.filhos.append(filho)

    def resumo(self):
        filhos_nomes = ', '.join([filho.nome for filho in self.filhos])
        return f'Mãe: {super().resumo()}, Filhos: {filhos_nomes}'

class Filho(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.pai = None
        self.mae = None

    def adicionar_pais(self, pai, mae):
        self.pai = pai
        self.mae = mae

    def resumo(self):
        pai_nome = self.pai.nome if self.pai else 'Desconhecido'
        mae_nome = self.mae.nome if self.mae else 'Desconhecido'
        return f'Filho: {super().resumo()}, Pai: {pai_nome}, Mãe: {mae_nome}'

# Exemplo de uso
pai = Pai('João', 40)
mae = Mae('Maria', 38)
filho1 = Filho('Pedro', 10)
filho2 = Filho('Ana', 8)

pai.adicionar_filho(filho1)
pai.adicionar_filho(filho2)
mae.adicionar_filho(filho1)
mae.adicionar_filho(filho2)

filho1.adicionar_pais(pai, mae)
filho2.adicionar_pais(pai, mae)

print(pai.resumo())
print(mae.resumo())
print(filho1.resumo())
print(filho2.resumo())