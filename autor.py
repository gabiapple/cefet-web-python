class Autor():
    def __init__(self, primeiro_nome, ultimo_nome, data_nascimento, nome_meio=''):
        self.primeiro_nome = primeiro_nome
        self.nome_meio = nome_meio
        self.ultimo_nome = ultimo_nome
        self.data_nascimento = data_nascimento

    def __str__(self):
        nome = " ".join([self.primeiro_nome, self.nome_meio, self.ultimo_nome])
        return "Autor: {}\n".format(nome)

    @property
    def nome_como_citado(self):
        return "{} {}.".format(self.ultimo_nome.upper(), self.primeiro_nome[0])

    @property
    def nome(self):
        return "{} {} {}".format(self.primeiro_nome, self.nome_meio, self.ultimo_nome)