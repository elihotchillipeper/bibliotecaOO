class Autor:
    def __init__(self, nome, nacionalidade):
        self.__nome = nome
        self.__nacionalidade = nacionalidade

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_nacionalidade(self):
        return self.__nacionalidade

    def set_nacionalidade(self, nacionalidade):
        self.__nacionalidade = nacionalidade

    def __str__(self):
        return f"{self.__nome} ({self.__nacionalidade})"

class Livro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__disponibilidade = True

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_autor(self):
        return self.__autor

    def set_autor(self, autor):
        self.__autor = autor

    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, isbn):
        self.__isbn = isbn

    def get_disponibilidade(self):
        return self.__disponibilidade

    def set_disponibilidade(self, disponibilidade):
        self.__disponibilidade = disponibilidade

    def adicionar(self, biblioteca):
        biblioteca.adicionar_livro(self)

    def buscar(self, biblioteca, termo):
        return biblioteca.buscar_livro(termo)

    def emprestar(self, usuario):
        if self.__disponibilidade:
            self.__disponibilidade = False
            usuario.adicionar_livro(self)
            return True
        return False

    def devolver(self, usuario):
        if not self.__disponibilidade:
            self.__disponibilidade = True
            usuario.remover_livro(self)
            return True
        return False

    def __str__(self):
        return f"{self.__titulo} por {self.__autor} (ISBN: {self.__isbn})"

class Usuario:
    def __init__(self, nome, id_usuario):
        self.__nome = nome
        self.__id_usuario = id_usuario
        self.__livros_emprestados = []

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_id_usuario(self):
        return self.__id_usuario

    def set_id_usuario(self, id_usuario):
        self.__id_usuario = id_usuario

    def adicionar_livro(self, livro):
        self.__livros_emprestados.append(livro)

    def remover_livro(self, livro):
        if livro in self.__livros_emprestados:
            self.__livros_emprestados.remove(livro)

    def __str__(self):
        livros = ', '.join(str(livro) for livro in self.__livros_emprestados)
        return f"Usuário: {self.__nome} (ID: {self.__id_usuario})\nLivros emprestados: {livros}"

class Biblioteca:
    def __init__(self):
        self.__livros = []
        self.__usuarios = []

    def adicionar_livro(self, livro):
        self.__livros.append(livro)

    def adicionar_usuario(self, usuario):
        self.__usuarios.append(usuario)

    def buscar_livro(self, termo):
        resultados = []
        for livro in self.__livros:
            if termo.lower() in livro.get_titulo().lower() or termo.lower() in livro.get_autor().get_nome().lower():
                resultados.append(livro)
        return resultados

    def buscar_usuario(self, id_usuario):
        for usuario in self.__usuarios:
            if usuario.get_id_usuario() == id_usuario:
                return usuario
        return None

    def __str__(self):
        livros = ', '.join(str(livro) for livro in self.__livros)
        usuarios = ', '.join(str(usuario) for usuario in self.__usuarios)
        return f"Biblioteca:\nLivros: {livros}\nUsuários: {usuarios}"

def exibir_menu():
    print("\nMenu:")
    print("1. Adicionar um livro")
    print("2. Adicionar um usuário")
    print("3. Buscar um livro")
    print("4. Emprestar um livro")
    print("5. Devolver um livro")
    print("6. Exibir informações da biblioteca")
    print("7. Sair")

def main():
    biblioteca = Biblioteca()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-7): ")

        if opcao == '1':
            titulo = input("Título do livro: ")
            nome_autor = input("Nome do autor: ")
            nacionalidade_autor = input("Nacionalidade do autor: ")
            isbn = input("ISBN do livro: ")
            autor = Autor(nome_autor, nacionalidade_autor)
            livro = Livro(titulo, autor, isbn)
            livro.adicionar(biblioteca)
            print("Livro adicionado com sucesso.")

        elif opcao == '2':
            nome_usuario = input("Nome do usuário: ")
            id_usuario = int(input("ID do usuário: "))
            usuario = Usuario(nome_usuario, id_usuario)
            biblioteca.adicionar_usuario(usuario)
            print("Usuário adicionado com sucesso.")

        elif opcao == '3':
            termo = input("Digite o título ou autor do livro para buscar: ")
            resultados = biblioteca.buscar_livro(termo)
            if resultados:
                for livro in resultados:
                    print(livro)
            else:
                print("Nenhum livro encontrado.")

        elif opcao == '4':
            id_usuario = int(input("ID do usuário: "))
            usuario = biblioteca.buscar_usuario(id_usuario)
            if usuario:
                termo = input("Digite o título ou autor do livro para emprestar: ")
                resultados = biblioteca.buscar_livro(termo)
                if resultados:
                    for i, livro in enumerate(resultados):
                        print(f"{i+1}. {livro}")
                    escolha = int(input("Escolha o número do livro para emprestar: ")) - 1
                    if 0 <= escolha < len(resultados):
                        livro = resultados[escolha]
                        if livro.emprestar(usuario):
                            print("Livro emprestado com sucesso.")
                        else:
                            print("Livro não disponível.")
                    else:
                        print("Escolha inválida.")
                else:
                    print("Nenhum livro encontrado.")
            else:
                print("Usuário não encontrado.")

        elif opcao == '5':
            id_usuario = int(input("ID do usuário: "))
            usuario = biblioteca.buscar_usuario(id_usuario)
            if usuario:
                termo = input("Digite o título ou autor do livro para devolver: ")
                resultados = biblioteca.buscar_livro(termo)
                if resultados:
                    for i, livro in enumerate(resultados):
                        print(f"{i+1}. {livro}")
                    escolha = int(input("Escolha o número do livro para devolver: ")) - 1
                    if 0 <= escolha < len(resultados):
                        livro = resultados[escolha]
                        if livro.devolver(usuario):
                            print("Livro devolvido com sucesso.")
                        else:
                            print("O livro não estava emprestado.")
                    else:
                        print("Escolha inválida.")
                else:
                    print("Nenhum livro encontrado.")
            else:
                print("Usuário não encontrado.")

        elif opcao == '6':
            print(biblioteca)

        elif opcao == '7':
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 7.")

if __name__ == "__main__":
    main()
