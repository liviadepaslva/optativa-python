class Carro:
    marca = "sem marca"
    modelo = "sem modelo"
    cor = "sem cor"
    ano = 0
    kmrodado = 0
    andando = False
    motorLigado = False

    def detalhes(self):
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("Cor: ", self.cor)
        print("Ano: ", self.ano)
        print("Km rodado: ", self.kmrodado)

    def status(self):
        print("Andando: ", self.andando)
        print("Motor ligado: ", self.motorLigado)
        
    def ligar(self):
        self.motorLigado = True
        print("Motor ligado")

    def desligar(self):
        self.motorLigado = False
        print("Motor desligado")
    
    def andar(self):
        if self.motorLigado:
            self.andando = True
            print("Andando")
        else:
            print("Ligue o motor")
    
    def parar(self):        
        self.andando = False
        print("Parado")

