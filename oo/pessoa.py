class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributo_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super.cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'


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
    Tiago.sobrenome = 'Ramos'
    del Tiago.filhos
    print(Tiago.__dict__)
    print(Leandro.__dict__)
    print(Pessoa.olhos)
    print(Tiago.olhos)
    print(Leandro.olhos)
