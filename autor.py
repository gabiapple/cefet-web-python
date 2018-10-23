class Autor():
    def __init__(self, primeiro_nome, nome_meio='', ultimo_nome, data_nascimento):
        self.primeiro_nome = primeiro_nome
        self.nome_meio = nome_meio
        self.ultimo_nome = ultimo_nome
        self.data_nascimento = data_nascimento

    def __str__(self):
        nome = " ".join([self.primeiro_nome, self.nome_meio, self.ultimo_nome])
        return "Nome: {}\nData de nascimento:{}".format(nome, self.data_nascimento)

    @property
    def nome_como_citado(self):
        return "{} {}.".format(self.ultimo_nome.to_upper(), self.primeiro_nome[0])
