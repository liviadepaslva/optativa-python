class Pessoa:
    def __init__(self, nome, idade, endereco, cpf, sexo):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.sexo = sexo

    def resumo(self):
        print(f'Nome: {self.nome}, Idade: {self.idade} anos, Endereço: {self.endereco}, CPF: {self.cpf}, Sexo: {self.sexo}')

class Pai(Pessoa):
    def __init__(self, nome, idade, endereco, cpf, sexo):
        super().__init__(nome, idade, endereco, cpf, sexo)
        self.filhos = []
        self.esposa = None

    def adicionar_filho(self, filho):
        self.filhos.append(filho)

    
    def adicionar_esposa(self, esposa):
        self.esposa = esposa

    def resumo(self):
        filhos_nomes = ', '.join([filho.nome for filho in self.filhos])
        super().resumo()
        print(f'Filhos: {filhos_nomes}, Esposa: {self.esposa.nome if self.esposa else "Nenhuma"}')

class Mae(Pessoa):
    def __init__(self, nome, idade, endereco, cpf, sexo):
        super().__init__(nome, idade, endereco, cpf, sexo)
        self.filhos = []
        self.esposo = None

    def adicionar_esposo(self, esposo):
        self.esposo = esposo

    def adicionar_filho(self, filho):
        self.filhos.append(filho)

    def resumo(self):
        filhos_nomes = ', '.join([filho.nome for filho in self.filhos])
        print(f'{super().resumo()}, Número de filhos: {len(self.filhos)}, Filhos: {filhos_nomes}')

class Filho(Pessoa):
    def __init__(self, nome, idade, endereco, cpf, sexo, pai, mae):
        super().__init__(nome, idade, endereco, cpf, sexo)
        self.pai = pai
        self.mae = mae

    def resumo(self):
        print(f'{super().resumo()}, Pai: {self.pai.nome}, Mãe: {self.mae.nome}')

    def adicionar_pai(self, pai):
        self.pai = pai
    
    def adicionar_mae(self, mae):
        self.mae = mae

pai = Pai('João', 40, 'Rua 1, 123', '123.456.789-00', 'M')
mae = Mae('Maria', 38, 'Rua 1, 123', '123.456.789-00', 'F')
filho1 = Filho('Pedro', 10, 'Rua 1, 123', '123.456.789-00', 'M', pai, mae)
filho2 = Filho('Ana', 8, 'Rua 1, 123', '123.456.789-00', 'F', pai, mae)

pai.adicionar_filho(filho1)
pai.adicionar_filho(filho2)
mae.adicionar_filho(filho1)
mae.adicionar_filho(filho2)

filho1.adicionar_pai(pai)
filho1.adicionar_mae(mae)
filho2.adicionar_pai(pai)
filho2.adicionar_mae(mae)

mae.resumo()
pai.resumo()

filho1.resumo()
filho2.resumo()