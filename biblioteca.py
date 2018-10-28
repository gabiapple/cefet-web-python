class Biblioteca():
    def __init__(self, livros):
        self.livros = livros

    def __str__(self):
        return "\n".join([str(livro) for livro in self.livros])
    
    @property

    def livros_por_autor(self):
        data = {}
        for livro in self.livros:
            for autor in livro.autores:

                if autor.nome not in data:
                    data[autor.nome] = []

                data[autor.nome].append(livro.titulo)

        return data