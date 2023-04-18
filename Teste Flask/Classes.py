class Restaurante:
    def __init__(self, id, nome, imagem, endereço, comentario):
        self.id = id
        self.nome = nome
        self.imagem = imagem
        self.endereço = endereço    
        self.comentario = comentario

class Comentario:
    def __init__(self, pessoa, opniao):
        self.pessoa = pessoa
        self.opniao = opniao
