class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    Leandro = Pessoa(nome='Leandro')
    Tiago = Pessoa(Leandro, nome='Tiago')
    print(Pessoa.cumprimentar(Tiago))
    print(Tiago.cumprimentar())
    print(id(Tiago))
    print(Tiago.nome)
    print(Tiago.idade)
    for filho in Tiago.filhos:
        print(filho.nome)
