class Bicicleta:
    def __init__(self, modelo=str, ano=int, cor=str, valor=float, andando=False) -> None:
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.cor = cor

    def buzinar(self):
        print('FOm! Fom!')

    
    def andar(self):

        self.andando = True
        self.buzinar()


bike_1 = Bicicleta('Monark', 1896, 'Branca', 2000)

bike_1.andar()