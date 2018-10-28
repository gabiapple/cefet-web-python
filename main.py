from autor import Autor
from livro import Livro
from biblioteca import Biblioteca

def main():
    autor1 = Autor(primeiro_nome='Gabriela',
                    nome_meio='Ramalho',
                    ultimo_nome='Santos',
                    data_nascimento='05/07/1996')

    autor2 = Autor(primeiro_nome='Sara',
                    ultimo_nome='Santos',
                    data_nascimento='24/05/1999')

    livro1 = Livro('Computacao Musical', 2018, [autor1])
    livro2 = Livro('Administracao', 2018, [autor2])

    biblioteca = Biblioteca([livro1, livro2])

    print(biblioteca)
    print(biblioteca.livros_por_autor)

if __name__ == "__main__":
    main()
