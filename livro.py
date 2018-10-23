class Livro():
    def __init__(self, titulo, ano, lista=[]):
        self._titulo = titulo
        self.ano = ano
        self.lista = lista

    @property

    def titulo(self):
        return self.titulo


    @titulo.setter

    def titulo(self, val):
        if val is None:
            raise ValueError("Erro: não é possível titulo vazio")

        self._titulo = val
