class Postagem:
    def __init__(self,  titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo #sao diferentes

class Comentario:
    def __init__(self, conteudo, autor):
        self.conteudo = conteudo
        self.autor = autor