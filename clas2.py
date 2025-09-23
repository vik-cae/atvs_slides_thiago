class Livro:
    def __init__(self, nome, autor, editora, paginas):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas

    def alterar_editora(self, nova_editora):
        self.editora = nova_editora
        print(f"editora auterada: {self.editora}")

    def listar_paginas(self):
        print(f"quantidade de paginas: {self.paginas}")

livro1 = Livro("assim q acaba", "Collen", "LBN", 300)
livro1.alterar_editora("JQT")
livro1.listar_paginas()