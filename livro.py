class Livro():
    def __init__(self, titulo, ano, autores=[]):
        self._titulo = titulo
        self.ano = ano
        self.autores = autores

    def __str__(self):
        autores =  [x.nome_como_citado for x in self.autores]
        return ", ".join([self.titulo, str(self.ano)] + autores)

    @property

    def titulo(self):
        return self._titulo


    @titulo.setter

    def titulo(self, val):
        if val is None:
            raise ValueError("Erro: não é possível titulo vazio")

        self._titulo = val
