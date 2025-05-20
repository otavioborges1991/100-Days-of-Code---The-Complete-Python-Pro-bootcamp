class Saudacao:
    def __init__(self, mensagem):
        self.mensagem = mensagem

    def exibir(self):
        print(self.mensagem)

saudacao = Saudacao("Hello, world!")
saudacao.exibir()